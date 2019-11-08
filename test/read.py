

# Enable Arrow-based columnar data transfers
spark.conf.set("spark.sql.execution.arrow.enabled", "true")

df = spark.read.load("data/userdata1.parquet")
