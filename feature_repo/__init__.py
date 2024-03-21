from pyspark.sql import SparkSession


def get_spark_session():
    return spark


def init_spark():
    global spark
    spark = (
        SparkSession.builder.master("local[*]")
        .appName(name="unittest")
        .config("spark.ui.enabled", "false")
        .config(
            "spark.driver.bindAddress",
            "0.0.0.0",
        )
        .getOrCreate()
    )


init_spark()
