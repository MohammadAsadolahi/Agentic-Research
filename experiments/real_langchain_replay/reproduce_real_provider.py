"""Reproduce LangChain issue #40853 offline against pinned installed releases.

Affected: langchain 1.4.2, langchain-anthropic 1.7.4.
Fixed: langchain 1.4.3, langchain-anthropic 1.7.5.
No live API calls or credentials needed.
"""
import argparse
import json
from importlib.metadata import version
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain.agents.factory import _patch_invalid_tool_calls
from langchain_anthropic import ChatAnthropic

def check_provider_contract():
    history = [
        HumanMessage("do the thing"),
        AIMessage(
            content=[{"type": "text", "text": "calling tool"}],
            invalid_tool_calls=[{
                "name": "search", "args": '{"q": "truncat',
                "id": "toolu_01ABC", "error": "truncated", "type": "invalid_tool_call",
            }],
        ),
        HumanMessage("continue"),
    ]
    repaired = _patch_invalid_tool_calls(history)
    synthetic = [m for m in repaired if isinstance(m, ToolMessage)]
    assert len(synthetic) == 1, synthetic
    assert synthetic[0].tool_call_id == "toolu_01ABC"
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620", api_key="fake")
    wire = model._get_request_payload(repaired)["messages"]
    uses = [
        b["id"] for m in wire
        for b in (m["content"] if isinstance(m.get("content"), list) else [])
        if isinstance(b, dict) and b.get("type") == "tool_use"
    ]
    results = [
        b["tool_use_id"] for m in wire
        for b in (m["content"] if isinstance(m.get("content"), list) else [])
        if isinstance(b, dict) and b.get("type") == "tool_result"
    ]
    orphans = [i for i in results if i not in uses]
    return {
        "langchain": version("langchain"),
        "langchain_anthropic": version("langchain-anthropic"),
        "local_repair": "pass",
        "wire_tool_use_ids": uses,
        "wire_tool_result_ids": results,
        "orphan_result_ids": orphans,
        "provider_contract": "fail" if orphans else "pass",
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--expect", choices=["pass", "fail"], required=True)
    args = parser.parse_args()
    result = check_provider_contract()
    print(json.dumps(result, indent=2, sort_keys=True))
    assert result["provider_contract"] == args.expect, result
