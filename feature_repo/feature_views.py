import os

from feast import (
    FeatureView,
)
from feast.field import Field
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import (
    SparkSource,
)
from feast.types import Int64, String

from feature_repo import get_feature_folder_path
from feature_repo.entities import user

sparksource_user_loan = SparkSource(
    path=os.path.join(get_feature_folder_path(), "loan_default_gen"),
    file_format="parquet",
    timestamp_field="txn_datetime",
    name="user_loan",
)

contact_stats_fv = FeatureView(
    name="user_info",
    entities=[user],
    schema=[
        Field(name="Age", dtype=Int64),
        Field(name="Education", dtype=String),
        Field(name="CreditScore", dtype=Int64),
        Field(name="MonthsEmployed", dtype=Int64),
    ],
    source=sparksource_user_loan,
    description="Calculate overall transaction behaviors of customer",
)
