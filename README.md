# AWS Serverless ETL Pipeline (S3 → Lambda → Glue → Athena)

This project demonstrates the design of a serverless ETL pipeline on AWS:

- **S3**: stores raw JSON data
- **Lambda**: validates and preprocesses incoming records
- **Glue**: transforms data and writes partitioned output (e.g., Parquet)
- **Athena**: queries the transformed data using SQL

The code in this repository simulates the logic of the Lambda and Glue jobs locally in Python so it can be understood and tested without an AWS account.

---

## 🏗 Architecture

1. Raw JSON files are uploaded to an S3 bucket.
2. An S3 event triggers a **Lambda function**:
   - Validates required fields
   - Filters out malformed records
   - Writes cleaned data to another S3 location
3. An **AWS Glue ETL job**:
   - Reads cleaned data
   - Normalizes and transforms fields
   - Writes partitioned output for analytics
4. **Athena** queries the curated data.

---

## 📂 Project Structure

- `src/lambda_function.py` – Lambda handler and validation logic
- `src/glue_job.py` – Glue-style ETL transformation logic
- `src/utils.py` – Shared helpers
- `data/sample_events.json` – Example input events
- `requirements.txt` – Python dependencies

---

## ▶️ Running Locally (Simulation)

```bash
pip install -r requirements.txt
python src/lambda_function.py
python src/glue_job.py
