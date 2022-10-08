# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:57:58 2022

@author: Alex
"""

import requests
from bs4 import BeautifulSoup
import re
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import datetime

import cv2
import numpy as np
import json



URL = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"


class Item(BaseModel):
    total: int
    destroyed: int
    damaged: int
    abandoned: int
    captured: int



app = FastAPI()



@app.get("/items/")
async def get_data():

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    res = soup.h3
    res=res.text
    losses = re.findall(r'\b\d+\b',res)
       
    losses = losses[0] + "," + losses[1] + "," + losses[2] + "," + losses[3] + "," + losses[4]   
    return(losses)


@app.get("/time/")
async def get_time():
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M")
    current_time = current_time.replace(':','')
    
    return(int(current_time))



@app.get("/test_image/")
async def get_test_image():
    """
    processes and returns the test image for display in json format
    """
    
    IMAGE_FILE = "./imgs/monochrome_test_card_scaled.png"

    img_in = cv2.imread(IMAGE_FILE)
    

    
    img_out = cv2.rotate(img_in, cv2.ROTATE_90_CLOCKWISE)
    img_out = cv2.flip(img_out,1)
    img_out = (img_out*(1/255)).astype(int)
    img_out = img_out[:,:,0]
    img_out = img_out.tolist()

    #convert to list of ints
    def binary_list_to_int(lst):
    
        out = int(bin(int(''.join(map(str, lst)), 2) << 1),2)
        return out

    def reverse_bits(lst):
        """
        flip bits (used for last 4 anodes
        """
    
        out = [(i*-1) + 1 for i in lst]
        return out

    #first split each row into 32 bit words
    #repeat first word 8 times to make it 32 bits
    display_image = [[ reverse_bits(8*row[99:95:-1]), row[95:63:-1], row[63:31:-1],row[31::-1]] for row in img_out]

    #then to int
    display_image = [[binary_list_to_int(word) for word in row] for row in display_image]

    json_compatible_item_data = jsonable_encoder(display_image)
    return JSONResponse(content=json_compatible_item_data)
