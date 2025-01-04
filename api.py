# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:18:53 2024

@author: SWRM
"""

from fastapi import FastAPI, File, UploadFile
import cv2
from io import BytesIO
import numpy as np
import uvicorn
import tensorflow as tf
from src.exception import CustomException
import sys
import mlflow
import dagshub




#Creating app instance
app=FastAPI() 
repo="my-first-repo"
name="Simbarashe-Mutyambizi"
dagshub.init(repo,name)
try:
    repo="my-first-repo"
    name="Simbarashe-Mutyambizi"
    dagshub.init(repo,name)
    model=mlflow.pyfunc.load_model("mlflow-artifacts:/832dce8f9c7d4ada8db55eb01924cc2e/18c7324dd47f4336b53e63703690e4ef/artifacts/model")
except Exception as e:
    raise CustomException(e,sys)
    
#classes list
classes={1:"Infested with corn borer", 0:"Currently not affected by corn borer"}


#function to read image file, transform to np array, normalize and expand dimensions
def load_image_tensor(data):
    try:
        image_matrix=np.array(cv2.imread(BytesIO(data))) 
        image_matrix=image_matrix/255
        image_expanded=np.expand_dims(image_matrix, 0)
        return image_expanded
    except Exception as e:
        raise CustomException(e,sys)
    

#creating route path for api to load to
@app.get("/")
def index():
    return {"Welcome to the corn borer image classification api"}

@app.post("predictions")
async def predict( file: UploadFile=File(...)):
    try:
        image_value=load_image_tensor(await file.read())
        class_value=np.argmax(model.predict(image_value))
        prediction=classes[class_value]
        return {prediction}
    except Exception as e:
        raise CustomException(e,sys)



