"""Offline replay of LangChain issue #38351 on real pinned upstream source.

The bug is a router return-value not present in its graph destination map.
No LLM API requests; fake model and synthetic tool-message middleware.
"""
import argparse
import json

from langchain.agents import create_agent
from langchain.agents.middleware.types import AgentMiddleware, ExtendedModelResponse
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.types import Command


class ToolBindFakeModel(GenericFakeChatModel):
    def bind_tools(self, tools, **kwargs):
        return self


@tool
def foo(x: int) -> int:
    """A trivial tool the agent can call."""
    return x + 1


class InjectToolMessageMiddleware(AgentMiddleware):
    name = "inject_tool_msg"

    def wrap_model_call(self, request, handler):
        response = handler(request)
        ai = response.result[0]
        if isinstance(ai, AIMessage) and ai.tool_calls:
            synthetic = [
                ToolMessage(content="cached", tool_call_id=call["id"], name=call["name"])
                for call in ai.tool_calls
            ]
            return ExtendedModelResponse(
                model_response=response,
                command=Command(update={"messages": synthetic}),
            )
        return response


def replay():
    fake = ToolBindFakeModel(messages=iter([
        AIMessage(content="", tool_calls=[
            {"name": "foo", "args": {"x": 1}, "id": "call_xyz", "type": "tool_call"},
        ]),
        AIMessage(content="unused"),
    ]))
    agent = create_agent(model=fake, tools=[foo], middleware=[InjectToolMessageMiddleware()])
    try:
        agent.invoke({"messages": [HumanMessage(content="hi")]})
    except KeyError as exc:
        if exc.args == ("model",):
            return {"local_tool_synthesis": "pass", "graph_routing_contract": "fail", "error": str(exc)}
        raise
    return {"local_tool_synthesis": "pass", "graph_routing_contract": "pass", "error": None}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--expect", choices=["pass", "fail"], required=True)
    args = parser.parse_args()
    result = replay()
    print(json.dumps(result, indent=2, sort_keys=True))
    assert result["graph_routing_contract"] == args.expect, result
