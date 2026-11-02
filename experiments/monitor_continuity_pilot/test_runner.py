"""Contract tests for the pilot's methodology, not empirical validation."""
import unittest
import runner


class PilotTests(unittest.TestCase):
    def test_all_cases_are_executable(self):
        for case in runner.CASES:
            with self.subTest(case=case.name):
                app, monitor = runner.materialize(case)
                observed = runner.exercise(app, monitor, runner.ROUTES)
                self.assertEqual(observed["outputs"], [f"done:{r}" for r in runner.ROUTES])
                self.assertEqual(observed["committed"], list(runner.ROUTES))

    def test_controls_remain_semantically_valid(self):
        for case in runner.CASES:
            if not case.faulty:
                with self.subTest(case=case.name):
                    app, monitor = runner.materialize(case)
                    self.assertFalse(runner.gate(app, monitor, case, "full_semantic_canaries"))

    def test_faults_break_an_independent_monitor_or_alert_invariant(self):
        for case in runner.CASES:
            if case.faulty:
                with self.subTest(case=case.name):
                    app, monitor = runner.materialize(case)
                    self.assertTrue(runner.gate(app, monitor, case, "full_semantic_canaries"))

    def test_count_accounting_does_not_imply_semantic_fidelity(self):
        for name in ("mislabel_tool", "redirect_alert_to_routine"):
            case = next(c for c in runner.CASES if c.name == name)
            app, monitor = runner.materialize(case)
            self.assertFalse(runner.gate(app, monitor, case, "count_reconciliation"))
            self.assertTrue(runner.gate(app, monitor, case, "full_semantic_canaries"))

    def test_cost_and_detection_summary_is_locked(self):
        report = runner.evaluate()
        self.assertEqual(len(report["cases"]), 14)
        self.assertEqual(report["metrics"]["single_routine_canary"]["true_positives"], 5)
        self.assertEqual(report["metrics"]["count_reconciliation"]["true_positives"], 8)
        self.assertEqual(report["metrics"]["full_semantic_canaries"]["true_positives"], 10)
        self.assertEqual(sum(v["false_positives"] for v in report["metrics"].values()), 0)


if __name__ == "__main__":
    unittest.main()
