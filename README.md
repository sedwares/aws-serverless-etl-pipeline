# AWS Serverless ETL Pipeline (S3 → Lambda → Glue → Athena)

This project demonstrates the design of a **serverless data pipeline** on AWS using:

- **Amazon S3** for raw data storage  
- **AWS Lambda** for event-driven validation and preprocessing  
- **AWS Glue** for ETL transformations  
- **Amazon Athena** for SQL-based analytics  

The code in this repository simulates the Lambda and Glue logic locally in Python so the pipeline can be understood and tested without an active AWS account.

---

## 🏗 Architecture Overview

1. Raw JSON events are uploaded to an S3 bucket.  
2. An S3 event triggers a **Lambda function** which:
   - Validates required fields  
   - Filters invalid records  
   - Writes cleaned data to a “curated” location  
3. An **AWS Glue job** reads the cleaned data and:
   - Normalizes the schema  
   - Enriches/derives new fields (e.g., buckets, type casting)  
   - Writes analytics-ready data (e.g., Parquet)  
4. **Athena** is used to query the curated dataset.

In this repo, S3 and Glue outputs are simulated using local files.

---

## 📂 Project Structure

```text
src/
  lambda_function.py  # validation + preprocessing (Lambda simulation)
  glue_job.py         # ETL transformation (Glue simulation)
  utils.py            # shared I/O helpers
data/
  sample_events.json  # raw example events
requirements.txt      # Python dependencies (pandas)
