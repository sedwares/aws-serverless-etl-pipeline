"""
Simulated AWS Glue ETL job.

Reads cleaned events, applies transformations, and prints summary stats.
"""

import pandas as pd
from utils import load_events


def run_glue_job():
    cleaned = load_events("clean_events.json")

    if not cleaned:
        print("No cleaned events found. Run lambda_function.py first.")
        return

    df = pd.DataFrame(cleaned)

    # Example transformation: derive a 'bucketed_value' and convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["value_bucket"] = pd.cut(df["value"], bins=[0, 10, 20, 50, 100], include_lowest=True)

    print("Schema:")
    print(df.dtypes)
    print("\nSample rows:")
    print(df.head())

    # In a real Glue job, we would write to S3 in Parquet format:
    # df.to_parquet("s3://curated-bucket/events/...", partition_cols=["value_bucket"])
    # Here we just write a CSV locally.
    df.to_csv("curated_events.csv", index=False)
    print("\nCurated data written to curated_events.csv")


if __name__ == "__main__":
    run_glue_job()
