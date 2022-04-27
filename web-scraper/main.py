# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:57:58 2022

@author: Alex
"""

import requests
from bs4 import BeautifulSoup
import re
from fastapi import FastAPI
from pydantic import BaseModel
import os
import datetime


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



