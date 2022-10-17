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
import json

from api_tools import image_tools



URL = "https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html"
TEST_IMAGE = "./imgs/image_sequence/6.PNG"
IMAGE_DIRECTORY = "./imgs/image_sequence/"

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



@app.get("/test_binary_image/")
async def get_test_binary_image():
    """
    processes and returns the test image for display in json format
    """
    
    display_image = image_tools.return_binary_image(TEST_IMAGE)
    json_compatible_item_data = jsonable_encoder(display_image)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/test_grayscale_image/")
async def get_test_grayscale_image():
    """
    process and return 2 arrays to be used for frame rate
    controlled 4 bit grayscale image
    """
    
    display_image = image_tools.return_grayscale_image(TEST_IMAGE)
    json_compatible_item_data = jsonable_encoder(display_image)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/grayscale_image/")
async def get_grayscale_image(image_id:str):
    
    """
    returns a numbered image from the image sequence folder
    """
    display_image = image_tools.return_grayscale_image(IMAGE_DIRECTORY + image_id + ".PNG")
    json_compatible_item_data = jsonable_encoder(display_image)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/waifu/")
async def get_waifu():
    
    display_image = image_tools.return_waifu()
    json_compatible_item_data = jsonable_encoder(display_image)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/stored_waifu/")
async def get_stored_waifu():
    
    display_image = image_tools.return_random_from_directory("imgs/anime_dataset/archive/images")
    json_compatible_item_data = jsonable_encoder(display_image)
    return JSONResponse(content=json_compatible_item_data)