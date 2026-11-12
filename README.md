# Feature Backfill Impact Planner

Feature backfills compete for compute. Operators need to compare downstream dependency and customer impact before choosing an order.

## What I built

I built a feature backfill ranking CLI. It combines backfill duration, downstream model count, estimated executor hours, and customer visibility into a score that reviewers can use to sequence work.

## How it works

```mermaid
flowchart LR
    A["Feature backfill CSV"]
    B["Weight backfill days, downstream models, compute, and visibility"]
    C["Rank by descending score"]
    D["Ordered feature group risk scores"]
    A --> B --> C --> D
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [backfill_planner.py](backfill_planner.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 backfill_planner.py sample_backfills.csv
```

Personalization ranks highest at 184.0, ahead of risk-signals and analytics-lite. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 backfill_planner.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The weights are a local policy. The CLI does not execute backfills or enforce compute limits.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
