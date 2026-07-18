import unittest

from backfill_planner import plan, risk_score


class BackfillPlannerTest(unittest.TestCase):
    def test_customer_visible_jobs_receive_extra_risk(self):
        base = {"days_to_backfill": "1", "downstream_models": "1", "estimated_executor_hours": "20", "customer_visible": "false"}
        visible = dict(base, customer_visible="true")
        self.assertGreater(risk_score(visible), risk_score(base))

    def test_plan_sorts_highest_risk_first(self):
        rows = [
            {"feature_group": "low", "days_to_backfill": "1", "downstream_models": "1", "estimated_executor_hours": "20", "customer_visible": "false"},
            {"feature_group": "high", "days_to_backfill": "10", "downstream_models": "5", "estimated_executor_hours": "200", "customer_visible": "true"},
        ]
        self.assertEqual(plan(rows)[0]["feature_group"], "high")


if __name__ == "__main__":
    unittest.main()
