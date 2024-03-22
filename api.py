from datetime import date
from typing import Any
import joblib
import numpy as np
import uvicorn

from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel
from feast import FeatureStore
from xgboost import XGBClassifier

from feature_repo import store

class Request(BaseModel):
    user_id: str
    loan_amount: float
    interest_rate: float
    loan_term: int
    dti_ratio:float

class Response(BaseModel):
    request: Request
    default_score: float


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    model=joblib.load('models/user_xgb_v1.joblib')
    ml_models['model'] = model
    ml_models['store']= store.get_store()
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.post("/predict_loan_default")
def predict_loan_default(request_loan_predict: Request) -> Response:
    store: FeatureStore=ml_models['store']
    xgb: XGBClassifier = ml_models['model']
    feature_dict={}
    user_id=request_loan_predict.user_id
    feature_dict['loan_amount']=request_loan_predict.loan_amount
    feature_dict['loan_term']=request_loan_predict.loan_term
    feature_dict['dti_ratio']=request_loan_predict.dti_ratio
    feature_dict['interest_rate']=request_loan_predict.interest_rate
    
    fs_model=store.get_feature_service('user_xgb_v1')
    features_from_store = store.get_online_features(
        features=fs_model, entity_rows=[{'user_id':user_id}]
    ).to_dict()
    list_feature=[]
    for feature in xgb.feature_names_in_:
        if feature not in feature_dict:
            feature_dict[feature]=features_from_store[feature][0]
    
        list_feature.append(feature_dict[feature])
    
    score=xgb.predict_proba(np.array([list_feature]))[0][1]
    
    
    response=Response(request=request_loan_predict,default_score=score)
    
    return response 
    
if __name__=='__main__':
    config = uvicorn.Config(
        "api:app", port=8000, log_level="info", workers=4, host='0.0.0.0',reload=True
    )
    server = uvicorn.Server(config)
    server.run()
    

