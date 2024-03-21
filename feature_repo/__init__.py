import os
from pyspark.sql import SparkSession

def get_spark_session():
    return spark


def init_spark():
    global spark
    os.environ['SPARK_LOCAL_IP']='127.0.0.1'
    spark = (
        SparkSession.builder.master("local[*]")
        .appName(name="unittest")
        .config("spark.ui.enabled", "false")
        .config(
            "spark.driver.bindAddress",
            "0.0.0.0",
        ).getOrCreate()
    )

def get_registry_path():
    return os.environ['REGISTRY_PATH']

def get_feature_folder_path():
    return os.environ['FEATURE_FOLDER_PATH']

init_spark()