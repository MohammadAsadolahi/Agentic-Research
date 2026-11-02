"""Unit tests of analysis arithmetic with simulated data. NOT agent experiments."""
import csv
import tempfile
import unittest
from pathlib import Path
from analyze import CELLS, analyze, parse_rows

FIELDS = ("task_id", "block_id", "parallel", "revision", "failure", "main_task_success", "cost_usd")


class TestAnalysis(unittest.TestCase):
    def make_csv(self, incomplete=False):
        directory = tempfile.TemporaryDirectory()
        path = Path(directory.name) / "example.csv"
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()
            for task in ["task-A", "task-B"]:
                for c, r in CELLS:
                    if incomplete and task == "task-B" and (c, r) == (1, 1):
                        continue
                    w.writerow(dict(task_id=task, block_id=task+"-seed-0",
                                    parallel=c, revision=r, failure=int(c and r),
                                    main_task_success=int(not(c and r)), cost_usd="0.25"))
        return directory, path

    def test_known_interaction_arithmetic(self):
        directory, path = self.make_csv()
        try:
            blocks = parse_rows(path)
            out = analyze(blocks, resamples=100)
            self.assertEqual(out["num_blocks"], 2)
            self.assertEqual(out["num_independent_task_ids"], 2)
            self.assertAlmostEqual(out["risk_difference_interaction"], 1.0)
            self.assertEqual(out["bootstrap_percentile_95"], [1.0, 1.0])
        finally:
            directory.cleanup()

    def test_reject_incomplete_experiment(self):
        directory, path = self.make_csv(incomplete=True)
        try:
            with self.assertRaisesRegex(ValueError, "Incomplete"):
                parse_rows(path)
        finally:
            directory.cleanup()

    def test_synthetic_fixture_is_not_misreported_as_real(self):
        self.assertIn("simulated", __doc__.lower())
        # No CSV data ships with the repository and this test writes temp files.
        self.assertFalse((Path(__file__).parent / "agent_runs.csv").exists())


if __name__ == "__main__":
    unittest.main()
