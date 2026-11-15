# Skills and verification

## What this repository demonstrates

A feature backfill ranking CLI. It combines backfill duration, downstream model count, estimated executor hours, and customer visibility into a score that reviewers can use to sequence work.

## Reproduce the result

Personalization ranks highest at 184.0, ahead of risk-signals and analytics-lite. Reproduce the primary fixture with `python3 backfill_planner.py sample_backfills.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The weights are a local policy. The CLI does not execute backfills or enforce compute limits.

Use the ranking to start a scheduling review. Confirm executor availability and dependencies before assigning a backfill slot.

[backfill_planner.py](../backfill_planner.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
