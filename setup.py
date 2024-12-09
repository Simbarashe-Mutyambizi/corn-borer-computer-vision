# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:28:41 2024

@author: SWRM
"""

from setuptools import setup,find_packages
from typing import List 

"""
Functionality: This file will install all the necessary requirements
               from requirements.txt file for an system that runs this project
               
"""

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
       requirements=file_obj.readlines()
       requirements=[req.replace("\n","") for req in requirements]
       
       if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)
   
    return requirements


setup(
      name="corn-borer-computer-vision",
      version="0.0.1",
      author="Simbarashe Mutyambizi",
      author_email="simbarashewilliammutyambizi@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
      
      
      
      
      )