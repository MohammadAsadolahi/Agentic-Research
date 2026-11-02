"""Freeze a feasibility split for ControlArena's 18 public Django side-task instances.

This produces *only* a task-ID split and validation checks. It DOES NOT run
agents, evaluate attacks, hide labels, or establish novelty.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

UPSTREAM_REPO = "UKGovernmentBEIS/control-arena"
UPSTREAM_COMMIT = "ae0b6fa78ace5a097536eb3464ab5a089740b53e"
SEED = "agentic-paper-2026-11-02-first-agent-control-feasibility"

# Captured from control_arena/settings/swebench/side_tasks/ at the pinned source.
IDS = (
    "django__django-12308", "django__django-13195",
    "django__django-13347", "django__django-13513",
    "django__django-13551", "django__django-13768",
    "django__django-14411", "django__django-14539",
    "django__django-14752", "django__django-15103",
    "django__django-15202", "django__django-15789",
    "django__django-15996", "django__django-16100",
    "django__django-16631", "django__django-16661",
    "django__django-16873", "django__django-16877",
)


def generate() -> dict:
    assert len(IDS) == 18 and len(set(IDS)) == 18
    ranked = sorted(IDS, key=lambda x: hashlib.sha256((SEED + ":" + x).encode()).hexdigest())
    development, holdout = sorted(ranked[:4]), sorted(ranked[4:])
    assert set(development).isdisjoint(holdout)
    assert set(development) | set(holdout) == set(IDS)
    return {
        "status": "task_split_only_no_agent_runs",
        "data_source": f"https://github.com/{UPSTREAM_REPO}/tree/{UPSTREAM_COMMIT}/control_arena/settings/swebench/side_tasks",
        "upstream_commit": UPSTREAM_COMMIT,
        "split_seed": SEED,
        "development_ids": development,
        "holdout_ids": holdout,
        "total_task_ids": len(IDS),
        "independent_samples": 0,
        "model_api_calls": 0,
        "warning": "All case files are public. This split does not conceal side tasks from models or create an unbiased benchmark. Fourteen holdouts are too few for high-powered safety claims.",
    }


def main() -> None:
    report = generate()
    path = Path("experiments/controlarena_paper_gate/split.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "development": len(report["development_ids"]),
        "holdout": len(report["holdout_ids"]),
        "agent_runs": 0,
        "claim": "design_frozen_not_evaluated",
    }))


if __name__ == "__main__":
    main()
