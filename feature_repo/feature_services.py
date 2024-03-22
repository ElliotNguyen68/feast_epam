from feast import FeatureService

from feature_repo.feature_views import user_info_fv, user_ts_feature_fv


user_feature_v1_fs = FeatureService(
    name="user_xgb_v1",
    features=[
        user_info_fv[
            [
                "Age",
                "CreditScore",
                "MonthsEmployed",
            ]
        ],
        user_ts_feature_fv[
            [
                "median_previous_income",
                "mean_previous_income",
                "mean_previous_default",
            ]
        ],
    ],
)
