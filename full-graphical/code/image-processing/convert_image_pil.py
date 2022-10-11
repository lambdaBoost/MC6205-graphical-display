from PIL import Image
import numpy as np
import json

IMAGE_FILE = "../imgs/monochrome_test_card_scaled.png"

image = Image.open(IMAGE_FILE)
image = image.rotate(90)
image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) 
img_out = np.asarray(image)

img_out = (img_out*(1/255)).astype(int)
img_out = img_out[:,:,0]
img_out = img_out.tolist()
    