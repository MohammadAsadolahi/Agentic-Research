"""Source-grounded offline reproducer from openai/openai-agents-python #4615.\nNo live model APIs. Historical failure injected in Session.add_items().\n"""\nimport asyncio
import json
import os
from typing import Any

from agents import Agent, RunConfig, RunState, Runner, function_tool
from agents.testing import ScriptedModel
from openai.types.responses import (
    ResponseFunctionToolCall,
    ResponseOutputMessage,
    ResponseOutputText,
)


class FailOnceSession:
    """A Session whose failed add is atomic: the rejected batch is not stored."""

    def __init__(self) -> None:
        self.session_id = "session-1"
        self.items: list[dict[str, Any]] = []
        self.fail_next_add = False

    async def get_items(self, limit: int | None = None) -> list[dict[str, Any]]:
        items = list(self.items)
        return items[-limit:] if limit is not None else items

    async def add_items(self, items: list[dict[str, Any]]) -> None:
        if self.fail_next_add:
            self.fail_next_add = False
            raise RuntimeError("injected atomic Session.add_items failure")
        self.items.extend(items)

    async def pop_item(self) -> dict[str, Any] | None:
        return self.items.pop() if self.items else None

    async def clear_session(self) -> None:
        self.items.clear()


def count(items: list[dict[str, Any]], item_type: str) -> int:
    return sum(
        item.get("type") == item_type and item.get("call_id") == "call-charge"
        for item in items
    )


async def main() -> None:
    model = ScriptedModel(
        steps=[
            [
                ResponseFunctionToolCall(
                    id="fc-1",
                    call_id="call-charge",
                    type="function_call",
                    name="charge",
                    arguments=json.dumps({"amount": 7}),
                )
            ],
            [
                ResponseOutputMessage(
                    id="msg-1",
                    type="message",
                    role="assistant",
                    content=[
                        ResponseOutputText(
                            type="output_text",
                            text="done",
                            annotations=[],
                            logprobs=[],
                        )
                    ],
                    status="completed",
                )
            ],
        ]
    )

    effects: list[int] = []

    @function_tool(needs_approval=True)
    async def charge(amount: int) -> str:
        effects.append(amount)
        return f"charged:{amount}"

    agent = Agent(name="agent", model=model, tools=[charge])
    session = FailOnceSession()
    config = RunConfig(tracing_disabled=True)

    paused = await Runner.run(agent, "charge 7", session=session, run_config=config)
    state = paused.to_state()
    state.approve(state.get_interruptions()[0])

    session.fail_next_add = True
    try:
        await Runner.run(agent, state, session=session, run_config=config)
    except RuntimeError as error:
        print("first resume:", error)

    print("step after failure:", state.to_json()["current_step"]["type"])
    print("effects after failure:", effects)

    # A JSON round-trip here produces the same result:
    # state = await RunState.from_json(agent, state.to_json())

    resumed = await Runner.run(agent, state, session=session, run_config=config)
    replay = resumed.to_input_list()

    print("final output:", resumed.final_output)
    print("effects after retry:", effects)
    print(
        "Session call/output:",
        count(session.items, "function_call"),
        count(session.items, "function_call_output"),
    )
    print(
        "Replay call/output:",
        count(replay, "function_call"),
        count(replay, "function_call_output"),
    )


    # Source-independent invariant: completed side effect must be represented in
    # durable history exactly once after a recoverable append failure.
    expected = os.environ.get("EXPECT_SESSION_PAIR")
    observed = (count(session.items, "function_call"), count(session.items, "function_call_output"))
    assert effects == [7], effects
    assert (count(replay, "function_call"), count(replay, "function_call_output")) == (1, 1)
    if expected == "broken":
        assert observed == (1, 0), observed
    elif expected == "fixed":
        assert observed == (1, 1), observed
    else:
        raise ValueError("EXPECT_SESSION_PAIR must be broken or fixed")
    print("Verified:", expected, "durable counts:", observed)


asyncio.run(main())
