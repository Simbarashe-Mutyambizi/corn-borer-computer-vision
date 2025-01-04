# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:13:58 2025

@author: SWRM
"""
import os
import wget
model_path=os.path.join(os.getcwd(),"model")
os.makedirs(model_path,exist_ok=True)
os.chdir(model_path)
wget.download("mlflow-artifacts:/832dce8f9c7d4ada8db55eb01924cc2e/18c7324dd47f4336b53e63703690e4ef/artifacts/model/data/model.keras")