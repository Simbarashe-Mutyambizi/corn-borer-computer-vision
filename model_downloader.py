# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:13:58 2025

@author: SWRM
"""
import os
import dagshub
import pickle
import mlflow

model_path=os.path.join(os.getcwd(),"model")
os.makedirs(model_path,exist_ok=True)
os.chdir(model_path)


repo="my-first-repo"
name="Simbarashe-Mutyambizi"
dagshub.auth.add_app_token(token="c751b2e61cc4e223562618c9fa391e9b3c6ab576")
dagshub.init(repo,name)
ml=mlflow.pyfunc.load_model("mlflow-artifacts:/832dce8f9c7d4ada8db55eb01924cc2e/18c7324dd47f4336b53e63703690e4ef/artifacts/model")
with open('saved_model.pkl', 'wb') as f:
    pickle.dump(ml, f)
