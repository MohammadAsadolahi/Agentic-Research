"""Run: python -m unittest discover -v (from this directory)."""
import unittest
from protocol_witness import (
    InvalidCall, anthropic_wire, orphan_result_ids, repair_history,
    result_matrix, unit_check_local_repair,
)


class TestChangeAwareBoundaryWitness(unittest.TestCase):
    def test_before_repair_cannot_create_orphan(self):
        history = repair_history([InvalidCall("a", "search")], enabled=False)
        self.assertEqual(orphan_result_ids(anthropic_wire(history, fixed=False)), [])

    def test_local_unit_pass_does_not_imply_provider_contract(self):
        calls = [InvalidCall("a", "search")]
        history = repair_history(calls, enabled=True)
        self.assertTrue(unit_check_local_repair(history, 1))
        self.assertEqual(orphan_result_ids(anthropic_wire(history, fixed=False)), ["a"])

    def test_provider_fix_restores_contract(self):
        calls = [InvalidCall("a", "search")]
        history = repair_history(calls, enabled=True)
        self.assertEqual(orphan_result_ids(anthropic_wire(history, fixed=True)), [])

    def test_multiple_results_need_matching_use(self):
        calls = [InvalidCall("a", "search"), InvalidCall("b", "browser")]
        history = repair_history(calls, enabled=True)
        self.assertEqual(orphan_result_ids(anthropic_wire(history, fixed=False)), ["a", "b"])
        self.assertEqual(orphan_result_ids(anthropic_wire(history, fixed=True)), [])

    def test_orphan_check_is_temporal(self):
        payload = [
            {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "a"}]},
            {"role": "assistant", "content": [{"type": "tool_use", "id": "a"}]},
        ]
        self.assertEqual(orphan_result_ids(payload), ["a"])

    def test_unmatched_result_is_detected_even_with_other_use(self):
        payload = [
            {"role": "assistant", "content": [{"type": "tool_use", "id": "a"}]},
            {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "b"}]},
        ]
        self.assertEqual(orphan_result_ids(payload), ["b"])

    def test_empty_history_has_no_orphans(self):
        self.assertEqual(orphan_result_ids([]), [])

    def test_matrix_shows_new_regression_after_local_fix(self):
        versions = {row["variant"]: row for row in result_matrix()}
        self.assertTrue(versions["before_repair"]["wire_contract_pass"])
        self.assertTrue(versions["local_repair_only"]["local_repair_unit_pass"])
        self.assertFalse(versions["local_repair_only"]["wire_contract_pass"])
        self.assertTrue(versions["local_and_provider_fix"]["wire_contract_pass"])


if __name__ == "__main__":
    unittest.main()
