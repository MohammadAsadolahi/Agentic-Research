"""Check preregistration integrity. Not an agent-evaluation test."""
import hashlib
import unittest
from prepare_split import IDS, SEED, UPSTREAM_COMMIT, generate


class SplitTests(unittest.TestCase):
    def test_partition_is_exhaustive_and_disjoint(self):
        m = generate()
        self.assertEqual(len(m["development_ids"]), 4)
        self.assertEqual(len(m["holdout_ids"]), 14)
        self.assertEqual(set(m["development_ids"]) & set(m["holdout_ids"]), set())
        self.assertEqual(set(m["development_ids"]) | set(m["holdout_ids"]), set(IDS))

    def test_input_manifest_has_expected_upstream_identifiers(self):
        self.assertEqual(len(IDS), 18)
        self.assertTrue(all(x.startswith("django__django-") for x in IDS))
        self.assertEqual(UPSTREAM_COMMIT, "ae0b6fa78ace5a097536eb3464ab5a089740b53e")

    def test_independently_calculated_hash_sort(self):
        m = generate()
        ranking = sorted(IDS, key=lambda x: hashlib.sha256((SEED + ":" + x).encode()).hexdigest())
        self.assertEqual(sorted(ranking[:4]), m["development_ids"])

    def test_never_claim_implemented_agent_eval(self):
        m = generate()
        self.assertEqual(m["independent_samples"], 0)
        self.assertEqual(m["model_api_calls"], 0)
        self.assertEqual(m["status"], "task_split_only_no_agent_runs")


if __name__ == "__main__":
    unittest.main()
