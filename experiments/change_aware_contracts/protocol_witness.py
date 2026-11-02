"""Dependency-free abstraction of a documented LangChain/Anthropic regression.

Historical reference:
  https://github.com/langchain-ai/langchain/pull/40530
  https://github.com/langchain-ai/langchain/issues/40853
  https://github.com/langchain-ai/langchain/pull/40864

This models a message-serialization invariant; it is NOT a reproduction of
real LangChain or Anthropic SDK versions and has no LLM calls.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class InvalidCall:
    identifier: str
    name: str
    malformed_arguments: str = "{"


def repair_history(calls: list[InvalidCall], *, enabled: bool) -> list[dict]:
    history = []
    for call in calls:
        history.append({"role": "assistant", "invalid_tool_call": call})
        if enabled:
            history.append({"role": "tool", "tool_result_id": call.identifier, "error": True})
    return history


def anthropic_wire(history: list[dict], *, fixed: bool) -> list[dict]:
    wire = []
    for msg in history:
        if msg["role"] == "assistant":
            call: InvalidCall = msg["invalid_tool_call"]
            blocks = []
            if fixed and call.identifier and call.name:
                blocks.append({"type": "tool_use", "id": call.identifier, "name": call.name})
            wire.append({"role": "assistant", "content": blocks})
        else:
            wire.append({"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": msg["tool_result_id"]}
            ]})
    return wire


def unit_check_local_repair(history: list[dict], expected_calls: int) -> bool:
    return sum(1 for msg in history if msg["role"] == "tool") == expected_calls


def orphan_result_ids(wire: list[dict]) -> list[str]:
    seen: set[str] = set()
    orphans = []
    for msg in wire:
        for block in msg["content"]:
            if block["type"] == "tool_use":
                seen.add(block["id"])
            if block["type"] == "tool_result" and block["tool_use_id"] not in seen:
                orphans.append(block["tool_use_id"])
    return orphans


def result_matrix(calls: list[InvalidCall] | None = None) -> list[dict]:
    calls = calls if calls is not None else [InvalidCall("toolu_01ABC", "search")]
    configs = [
        ("before_repair", False, False),
        ("local_repair_only", True, False),
        ("local_and_provider_fix", True, True),
    ]
    rows = []
    for version, repaired, serializer_fixed in configs:
        hist = repair_history(calls, enabled=repaired)
        wire = anthropic_wire(hist, fixed=serializer_fixed)
        rows.append({
            "variant": version,
            "local_repair_unit_pass": unit_check_local_repair(hist, len(calls)) if repaired else None,
            "wire_orphan_count": len(orphan_result_ids(wire)),
            "wire_contract_pass": not orphan_result_ids(wire),
        })
    return rows


if __name__ == "__main__":
    import json
    print(json.dumps(result_matrix(), indent=2))
