import unittest
from test_selector import select_checks, illustrative_path_only_baseline

class SelectionTests(unittest.TestCase):
    path = "libs/langchain_v1/langchain/agents/factory.py"

    def test_provider(self):
        self.assertEqual(select_checks(self.path, {"_patch_invalid_tool_calls"}), ["real_provider_replay"])

    def test_router(self):
        self.assertEqual(select_checks(self.path, {"model_to_tools_destinations"}), ["graph_route_contract"])

    def test_unrelated_edit(self):
        self.assertEqual(select_checks(self.path, {"other"}), [])

    def test_unrelated_path(self):
        self.assertEqual(select_checks("other.py", {"_patch_invalid_tool_calls"}), [])

    def test_both(self):
        self.assertEqual(select_checks(self.path, {"_patch_invalid_tool_calls", "model_to_tools_destinations"}),
                         ["graph_route_contract", "real_provider_replay"])

    def test_weak_path_baseline(self):
        self.assertEqual(illustrative_path_only_baseline(self.path), ["factory_local_tests"])

if __name__ == "__main__":
    unittest.main()
