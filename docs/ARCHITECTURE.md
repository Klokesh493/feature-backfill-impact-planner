# Feature Backfill Impact Planner architecture

Ranks ML feature backfills by customer impact, compute pressure, and downstream dependency count.

```mermaid
flowchart LR
    N0["sample_backfills.csv"]
    N1["backfill_planner.py"]
    N2["risk score / plan"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
