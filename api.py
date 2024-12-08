# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:18:53 2024

@author: SWRM
"""

from fastapi import FastAPI, File, UploadFile
import cv2
from io import BytesIO
import mlflow
import numpy as np
import uvicorn


#Creating app instance
app=FastAPI() 

#load model from mlflow
model_name="corn-borer-cnn"
model_url=f"models:/{model_name}/@champion"
model=mlflow.pyfunc.load_model(model_url)

#classes list
classes={1:"Infested with corn borer", 0:"Currently not affected by corn borer"}


#function to read image file, transform to np array, normalize and expand dimensions
def load_image_tensor(data):
    image_matrix=np.array(cv2.imread(BytesIO(data))) 
    image_matrix=image_matrix/255
    image_expanded=np.expand_dims(image_matrix, 0)
    return image_expanded
    

#creating route path for api to load to
@app.get("/")
def index():
    return {"Welcome to the corn borer image classification api"}

@app.post("predictions")
async def predict( file: UploadFile=File(...)):
    image_value=load_image_tensor(await file.read())
    class_value=np.argmax(model.predict(image_value))
    prediction=classes[class_value]
    return {prediction}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

