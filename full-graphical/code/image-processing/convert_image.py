# -*- coding: utf-8 -*-
import cv2
import numpy as np
import json

IMAGE_FILE = "../imgs/monochrome_test_card_scaled.png"

img_in = cv2.imread(IMAGE_FILE)
img_out = cv2.rotate(img_in, cv2.ROTATE_90_CLOCKWISE)
img_out = (img_out*(1/255)).astype(int)
img_out = img_out[:,:,0]
img_out = img_out.tolist()

with open('../imgs/test_card_json.json', 'w') as f:
    json.dump(img_out,f)
