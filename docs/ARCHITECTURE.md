# Feature Backfill Impact Planner architecture

Ranks ML feature backfills by customer impact, compute pressure, and downstream dependency count.

```mermaid
flowchart LR
    A["Feature backfill CSV"]
    B["Weight backfill days, downstream models, compute, and visibility"]
    C["Rank by descending score"]
    D["Ordered feature group risk scores"]
    A --> B --> C --> D
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
