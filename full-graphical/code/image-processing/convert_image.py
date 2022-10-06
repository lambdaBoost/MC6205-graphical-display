# -*- coding: utf-8 -*-
import cv2
import numpy as np
import json

IMAGE_FILE = "../imgs/monochrome_test_card_scaled.png"

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


with open('../imgs/test_card_json.json', 'w') as f:
    json.dump(display_image,f)
