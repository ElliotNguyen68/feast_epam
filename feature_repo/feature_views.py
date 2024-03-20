import os
from feast import (
     FeatureView,
     Field,
)
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import SparkSource
from feast.types import Float32, Int64,String


from feature_repo.entities import user


sparksource_user_loan=SparkSource(
    path=f"loan_default_gen.parquet",
    file_format="parquet",
    timestamp_field="txn_datetime",
    name='user_loan'
)


contact_stats_fv = FeatureView(
    name="user_info",
    entities=[user],
    schema=[
        Field(name="Age", dtype=Int64),
        Field(name="Education", dtype=String),
    ],
    source=sparksource_user_loan,
    description='Calculate overall transaction behaviors of customer'
)
