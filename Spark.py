import pyspark

# Create Spark session
spark = pyspark.sql.SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.driver.extraClassPath", "postgresql-42.7.4.jar") \
    .getOrCreate()

# Read table from DB using Spark JDBC
movies_df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/etl_pipeline") \
    .option("dbtable", "movies") \
    .option("user", "your_name") \
    .option("password", "your_password") \
    .option("driver", "org.postgresql.Driver") \
    .load()

# Print the DataFrame
movies_df.show()
