import csv
import sys


def risk_score(row):
    score = int(row["days_to_backfill"]) * 2
    score += int(row["downstream_models"]) * 12
    score += float(row["estimated_executor_hours"]) / 20
    if row["customer_visible"].lower() == "true":
        score += 25
    return round(score, 1)


def plan(rows):
    ranked = [{"feature_group": row["feature_group"], "risk_score": risk_score(row)} for row in rows]
    return sorted(ranked, key=lambda item: item["risk_score"], reverse=True)


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in plan(csv.DictReader(handle)):
            print(f'{item["feature_group"]}: {item["risk_score"]}')


if __name__ == "__main__":
    main(sys.argv[1])
