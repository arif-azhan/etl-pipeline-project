# ETL Pipeline Project

This project demonstrates an ETL (Extract, Transform, Load) pipeline using **PySpark** to extract data from a **PostgreSQL** database, process it, and display the results.

## Overview
The ETL pipeline connects to a PostgreSQL database using a JDBC driver, extracts data from a `movies` table, processes it using PySpark, and displays the transformed data in a DataFrame.

---

## Features
- **Extract**: Fetch data from a PostgreSQL database using PySpark and JDBC.
- **Transform**: Process and analyze data using PySpark DataFrames.
- **Load**: Showcase data transformations and output in a structured format.

---

## Tools & Technologies
- **PySpark**: For big data processing and transformation.
- **PostgreSQL**: As the relational database management system.
- **JDBC Driver**: To enable connectivity between PySpark and PostgreSQL.
- **Python**: Programming language for developing the pipeline.

---

## Prerequisites
Ensure you have the following installed:
1. **Python 3.8+**
2. **PySpark** (Install with `pip install pyspark`)
3. **PostgreSQL** (Running locally or remotely)
4. **PostgreSQL JDBC Driver** (Ensure the `.jar` file is included in the project)

---

## How to Set Up
### 1. Clone the Repository
```bash
git clone https://github.com/arif-azhan/etl-pipeline-project.git
cd etl-pipeline-project
```

### 2. Install Required Python Packages
Ensure you have PySpark installed:
```
pip install pyspark
```
 ### 3. Set Up the PostgreSQL Database
Create a database named etl_pipeline in PostgreSQL.
Populate the movies and users tables as required.

### 4. Update Configuration
Update the database credentials and JDBC driver path in the Spark.py file:
```
.option("url", "jdbc:postgresql://localhost:5432/etl_pipeline") \
.option("user", "your_postgres_username") \
.option("password", "your_postgres_password") \
.option("driver", "org.postgresql.Driver") \
.config("spark.driver.extraClassPath", "/path/to/postgresql-42.7.4.jar")
```

## How to Run
1. Start the PostgreSQL server:
```
brew services start postgresql
```
2. Run Spark.py script
```
python Spark.py
```

## Example Output
```
+---+--------------------+--------------------+--------+
| id|                name|         description|category|
+---+--------------------+--------------------+--------+
|  2|Avengers: Infinit...|Avengers: Infinit...|  Sci-Fi|
|  3|            Holidate|Holidate is a 202...|  Romcom|
|  4|          Extraction|Extraction is a 2...|  Action|
|  5|           John Wick|John Wick is a 20...|  Action|
+---+--------------------+--------------------+--------+
```


