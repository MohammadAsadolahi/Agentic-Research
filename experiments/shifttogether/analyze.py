"""Analysis of actual paired 2x2 agent experiments; NEVER generates results.

Usage:
    python experiments/shifttogether/analyze.py path/to/agent_runs.csv

Required columns:
task_id,block_id,parallel,revision,failure,main_task_success,cost_usd

Four cells (00,10,01,11) per block_id; multiple blocks may share a task.
Bootstrapping resamples entire tasks, not row-level or seed-level records.
"""
import argparse
import csv
import json
import random
from collections import defaultdict
from pathlib import Path

CELLS = ((0, 0), (1, 0), (0, 1), (1, 1))
NEEDED = {"task_id", "block_id", "parallel", "revision", "failure", "main_task_success", "cost_usd"}


def parse_rows(path):
    with open(path, encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not NEEDED <= set(reader.fieldnames or []):
            raise ValueError("Missing columns: " + ",".join(sorted(NEEDED - set(reader.fieldnames or []))))
        rows = list(reader)
    if not rows:
        raise ValueError("No real experiment rows supplied")
    grouped = defaultdict(dict)
    tasks = {}
    for r in rows:
        key = (int(r["parallel"]), int(r["revision"]))
        if key not in CELLS:
            raise ValueError("Cells must be binary")
        for field in ("failure", "main_task_success"):
            if r[field] not in ("0", "1"):
                raise ValueError(field + " must be binary")
        if float(r["cost_usd"]) < 0:
            raise ValueError("Negative cost")
        block = r["block_id"]
        if block in tasks and tasks[block] != r["task_id"]:
            raise ValueError("Block IDs must be unique across tasks")
        tasks[block] = r["task_id"]
        if key in grouped[block]:
            raise ValueError("Duplicate cell in block: " + block)
        grouped[block][key] = int(r["failure"])
    for block, cells in grouped.items():
        if set(cells) != set(CELLS):
            raise ValueError("Incomplete 2x2 block: " + block)
    return [(tasks[block], cells) for block, cells in sorted(grouped.items())]


def summarize(blocks):
    p = {f"{c}{r}": sum(cells[(c, r)] for _, cells in blocks) / len(blocks) for c, r in CELLS}
    interaction = p["11"] - p["10"] - p["01"] + p["00"]
    return {"failure_rate": p, "risk_difference_interaction": interaction}


def analyze(blocks, resamples=1000, seed=26021102):
    unique_tasks = sorted({task for task, _ in blocks})
    task_groups = {task: [b for b in blocks if b[0] == task] for task in unique_tasks}
    output = summarize(blocks)
    rng = random.Random(seed)
    estimates = []
    for _ in range(resamples):
        sampled_tasks = [rng.choice(unique_tasks) for _ in unique_tasks]
        sample = [block for task in sampled_tasks for block in task_groups[task]]
        estimates.append(summarize(sample)["risk_difference_interaction"])
    estimates.sort()
    lower = estimates[int(0.025 * resamples)]
    upper = estimates[min(resamples - 1, int(0.975 * resamples))]
    return {
        "analysis_type": "real_data_only_task_clustered_bootstrap",
        "num_blocks": len(blocks),
        "num_independent_task_ids": len(unique_tasks),
        **output,
        "bootstrap_percentile_95": [lower, upper],
        "statistical_warning": (
            "Task-level resampling does not repair selection bias, confounding, ceiling effects, "
            "insufficient task count or lack of genuine agent execution. Intervals may be unstable."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--bootstrap", type=int, default=1000)
    args = parser.parse_args()
    if args.bootstrap < 100:
        parser.error("Use at least 100 bootstrap samples")
    result = analyze(parse_rows(args.csv_path), resamples=args.bootstrap)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
