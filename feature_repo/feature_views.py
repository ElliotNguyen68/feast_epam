import os
from feast import (
     FeatureView,
     Field,
)
from feast.infra.offline_stores.contrib.spark_offline_store.spark_source import SparkSource
from feast.types import Float32, Int64,String
from feast.field import Field

from feature_repo.entities import user
from feature_repo import get_feature_folder_path


sparksource_user_loan=SparkSource(
    path=os.path.join(get_feature_folder_path(),'loan_default_gen'),
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
        Field(name="CreditScore", dtype=Int64),
        Field(name="MonthsEmployed", dtype=Int64),
    ],
    source=sparksource_user_loan,
    description='Calculate overall transaction behaviors of customer'
)

sparksource_user_loan_ts_feature=SparkSource(
    path=os.path.join(get_feature_folder_path(),'ts_feature'),
    file_format="parquet",
    timestamp_field="txn_datetime",
    name='user_ts_feature'
)


contact_ts_feature = FeatureView(
    name="user_loan_ts",
    entities=[user],
    schema=[
        Field(name="mean_previous_income", dtype=Float32),
        Field(name="max_previous_income", dtype=Float32),
        Field(name="min_previous_income", dtype=Float32),
        Field(name="median_previous_income", dtype=Float32),
        Field(name="quantile_25_previous_income", dtype=Float32),
        Field(name="quantile_75_previous_income", dtype=Float32),
        
        Field(name="mean_previous_age", dtype=Float32),
        Field(name="max_previous_age", dtype=Float32),
        Field(name="min_previous_age", dtype=Float32),
        Field(name="median_previous_age", dtype=Float32),
        Field(name="quantile_25_previous_age", dtype=Float32),
        Field(name="quantile_75_previous_age", dtype=Float32),
        
        Field(name="mean_previous_creditscore", dtype=Float32),
        Field(name="max_previous_creditscore", dtype=Float32),
        Field(name="min_previous_creditscore", dtype=Float32),
        Field(name="median_previous_creditscore", dtype=Float32),
        Field(name="quantile_25_previous_creditscore", dtype=Float32),
        Field(name="quantile_75_previous_creditscore", dtype=Float32),
        
        Field(name="mean_previous_default", dtype=Float32),
        Field(name="max_previous_default", dtype=Float32),
        Field(name="min_previous_default", dtype=Float32),
        Field(name="median_previous_default", dtype=Float32),
        Field(name="quantile_25_previous_default", dtype=Float32),
        Field(name="quantile_75_previous_default", dtype=Float32),
        
        Field(name="mean_previous_loan_amount", dtype=Float32),
        Field(name="max_previous_loan_amount", dtype=Float32),
        Field(name="min_previous_loan_amount", dtype=Float32),
        Field(name="median_previous_loan_amount", dtype=Float32),
        Field(name="quantile_25_previous_loan_amount", dtype=Float32),
        Field(name="quantile_75_previous_loan_amount", dtype=Float32),
        
        Field(name="mean_previous_loan_term", dtype=Float32),
        Field(name="max_previous_loan_term", dtype=Float32),
        Field(name="min_previous_loan_term", dtype=Float32),
        Field(name="median_previous_loan_term", dtype=Float32),
        Field(name="quantile_25_previous_loan_term", dtype=Float32),
        Field(name="quantile_75_previous_loan_term", dtype=Float32),  
       
        Field(name="mean_previous_", dtype=Float32),
        Field(name="max_previous_loan_term", dtype=Float32),
        Field(name="min_previous_loan_term", dtype=Float32),
        Field(name="median_previous_loan_term", dtype=Float32),
        Field(name="quantile_25_previous_loan_term", dtype=Float32),
        Field(name="quantile_75_previous_loan_term", dtype=Float32),   
        
    ],
    source=sparksource_user_loan_ts_feature,
    description='Calculate feature time series of customer'
)



