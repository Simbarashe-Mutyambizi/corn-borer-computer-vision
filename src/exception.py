# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:42:19 2024

@author: SWRM
"""

import sys
from src.logger import logging

def error_contents(error,error_details:sys):
    '''
    Functionality: This code will extract the error message, filename and
                   line of which the error occurred in
    Output       : Error message               
    '''
    _,_,error_info=error_details.exc_info()
    error_filename=error_info.tb_frame.f_code.co_filename
    error_message="Error occurred in python file [{0}] on line number [{1}] with error message being [{2}]".format(
        error_filename,error_filename.tb_lineno,str(error))
    


class CustomException (Exception):
    def __init__(self,error_message,error_details:sys):
        super.__init__(error_message)
        self.error_message=error_contents(error_message,error_details=error_details)
            
    def __str__ (self):
        return self.error_message
    
       
    