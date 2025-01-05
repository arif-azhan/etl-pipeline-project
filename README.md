# ETL Pipeline Project

This repository demonstrates an ETL (Extract, Transform, Load) pipeline built using Apache Airflow and Apache Spark, extracting data from PostgreSQL, transforming it using Spark, and loading it back into the database. It serves as a hands-on demonstration of modern data engineering practices.

## Project Structure
<img width="651" alt="Screenshot 2025-01-06 at 2 37 49 AM" src="https://github.com/user-attachments/assets/556dc737-c78f-4f7a-9e6d-0276927a4263" />



## Features

- **Extraction:** Data is extracted from PostgreSQL tables (`movies` and `users`) using Spark.
- **Transformation:** Data is aggregated (average ratings) and joined to create an enriched dataset.
- **Loading:** Transformed data is loaded into a new table in the PostgreSQL database (`avg_ratings`).
- **Orchestration:** Apache Airflow schedules and monitors the ETL pipeline using the DAG defined in `dag.py`.

## How It Works

### ETL Pipeline
1. **Extract:** Spark reads data from PostgreSQL.
2. **Transform:** Perform transformations, including joins and aggregations.
3. **Load:** Save the final DataFrame back to PostgreSQL.

### Apache Airflow
- The pipeline is orchestrated using Airflow, with tasks defined in a Python DAG (`dag.py`).
- Tasks are modular for better debugging and scalability.

## How to Run the Project

### Prerequisites
- **Python 3.12**
- **PostgreSQL**
- **Apache Airflow**
- **Apache Spark**

### Steps

1. **Set up virtual environment:**
   ```
   python3 -m venv airflow_env
   source airflow_env/bin/activate
   pip install -r requirements.txt
   ```

2. **Start Airflow Services:**
   ```
   airflow db init
   airflow scheduler
   airflow webserver
   ```

## Access the Airflow Web Interface:
Navigate to http://localhost:8080 in your browser.


# Database Setup
Load the datasets (movies.csv and users.csv) into PostgreSQL.
Update the connection details in ETL_Full_Script.py.
