# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 backfill_planner.py sample_backfills.csv
personalization: 184.0
risk-signals: 116.5
analytics-lite: 78.0
test_customer_visible_jobs_receive_extra_risk (test_backfill_planner.BackfillPlannerTest) ... ok
test_plan_sorts_highest_risk_first (test_backfill_planner.BackfillPlannerTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
````
