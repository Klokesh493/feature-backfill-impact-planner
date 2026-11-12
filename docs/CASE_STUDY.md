# Feature Backfill Impact Planner walkthrough

## Business problem

Ranks ML feature backfills by customer impact, compute pressure, and downstream dependency count.

## Reproduce the workflow

Run `python3 backfill_planner.py sample_backfills.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
personalization: 184.0
risk-signals: 116.5
analytics-lite: 78.0
```

The sample supplies these fields. `feature_group`, `days_to_backfill`, `downstream_models`, `estimated_executor_hours`, `customer_visible`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
