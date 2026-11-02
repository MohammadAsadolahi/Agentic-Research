# Monitor continuity: synthetic baseline comparator

This is a deterministic, hand-authored Python pilot, **not** a real coding-agent benchmark, incident reproduction, or novel algorithm.

Run from repository root:

    python experiments/monitor_continuity_pilot/runner.py --json pilot-results.json
    python -m unittest discover -s experiments/monitor_continuity_pilot -v

Requirements: Python 3.10+ standard library, no external API keys or model calls. The runner compiles and executes only its own static, experiment-authored source templates.

Four controls and ten deliberately faulty edits retain business-task outputs. The external evaluator checks monitoring identities and required alerts. The strongest baseline (complete-path semantic canaries) catches all ten authored faults; count-only reconciliation misses two cases where counts are correct but meanings are wrong. This is **not** a statistical detection-rate result, and the strongest canary was designed with full knowledge of the faults.

| Baseline | Faults caught / 10 | False positives / 4 | Route calls |
| --- | ---: | ---: | ---: |
| Protected monitoring file | 1 | 0 | 0 |
| Lexical call presence | 0 | 0 | 0 |
| Business output check | 0 | 0 | 1 |
| One-route canary | 5 | 0 | 1 |
| Count reconciliation | 8 | 0 | 3 |
| Full semantic canary | 10 | 0 | 3 |

See the detailed [research audit](../../research/2026-11-02_MONITOR_CONTINUITY_BASELINE_PILOT.md) for upstream prior art, caveats, and real-code falsification gates.
