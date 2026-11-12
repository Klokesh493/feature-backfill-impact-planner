# Feature Backfill Impact Planner

Ranks ML feature backfills by customer impact, compute pressure, and downstream dependency count.

Focus: feature platform, Spark backfills, operational risk, SRE prioritization.

Portfolio framing: Apple-scale client-style AI/ML platform project using synthetic data only.

## Run

```bash
python3 backfill_planner.py sample_backfills.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

Feature backfills compete for compute. Operators need to compare downstream dependency and customer impact before choosing an order.

## Project walkthrough

```mermaid
flowchart LR
    A["Feature backfill CSV"]
    B["Weight backfill days, downstream models, compute, and visibility"]
    C["Rank by descending score"]
    D["Ordered feature group risk scores"]
    A --> B --> C --> D
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 backfill_planner.py sample_backfills.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
