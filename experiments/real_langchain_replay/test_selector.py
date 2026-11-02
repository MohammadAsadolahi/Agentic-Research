"""Retrospective, manually annotated change-to-boundary-check mapping.

NOT a new algorithm, or fair comparison to coverage-based test selection.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Contract:
    name: str
    producer: str
    symbols: frozenset[str]
    test: str

CONTRACTS = (
    Contract("provider_tool_result_pairing", "libs/langchain_v1/langchain/agents/factory.py",
             frozenset({"_patch_invalid_tool_calls", "_invalid_tool_call_message"}), "real_provider_replay"),
    Contract("graph_route_destination", "libs/langchain_v1/langchain/agents/factory.py",
             frozenset({"model_to_tools_destinations", "middleware_w_wrap_model_call"}), "graph_route_contract"),
)

def select_checks(modified_path: str, changed_symbols: set[str]) -> list[str]:
    return sorted({c.test for c in CONTRACTS
                   if c.producer == modified_path and bool(c.symbols & changed_symbols)})

def illustrative_path_only_baseline(path: str) -> list[str]:
    return ["factory_local_tests"] if path.endswith("agents/factory.py") else []

if __name__ == "__main__":
    path = "libs/langchain_v1/langchain/agents/factory.py"
    for issue, sym in [("#40853", {"_patch_invalid_tool_calls"}), ("#38351", {"model_to_tools_destinations"})]:
        print(issue, "local", illustrative_path_only_baseline(path), "boundaries", select_checks(path, sym))
