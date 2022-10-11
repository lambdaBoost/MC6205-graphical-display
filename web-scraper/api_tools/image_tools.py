from PIL import Image
import numpy as np


def binarize(img):
    """
    convert raw image to binary
    """

    #initialize threshold
    thresh=128
    #convert image to greyscale
    img=img.convert('L') 
    width,height=img.size

    #traverse through pixels 
    for x in range(width):
        for y in range(height):

          #if intensity less than threshold, assign white
          if img.getpixel((x,y)) < thresh:
            img.putpixel((x,y),0)

          #if intensity greater than threshold, assign black 
          else:
            img.putpixel((x,y),255)

    return img


def img_to_4bit(img):
    """
    convert image to 4 bit grayscale with values 0-3
    """
    img=img.convert('L')
    img = np.asarray(img)
    img = img//64
    
    return img

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



def return_binary_image(file, save = False):

    
    image = Image.open(file)
    image = image.resize((100,100)) #simple resizing for now
    
    image=binarize(image)
    
    if save:
        image.save('./imgs/binary-test.png')
    
    image = image.rotate(90)
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) 
    img_out = np.asarray(image)
    

    img_out = (img_out*(1/255)).astype(int)
    #img_out = img_out[:,:,0]
    img_out = img_out.tolist()


    #first split each row into 32 bit words
    #repeat first word 8 times to make it 32 bits
    display_image = [[ reverse_bits(8*row[99:95:-1]), row[95:63:-1], row[63:31:-1],row[31::-1]] for row in img_out]

    #then to int
    display_image = [[binary_list_to_int(word) for word in row] for row in display_image]


def return_grayscale_image(file, save = False):
    """
    process and return 2 arrays to be used for frame rate
    controlled 4 bit grayscale image
    """
    image = Image.open(file)
    image = image.resize((100,100)) #simple resizing for now
    image = image.rotate(90)
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT) 
    
    image = img_to_4bit(image)
    
    img1 = (image >> 0) %2
    img2 = (image >> 1) %2
    
    if save:
        
        img1_png = img1*255
        img1_png = Image.fromarray(img1_png)
        
        img2_png = img2*255
        img2_png = Image.fromarray(img2_png)
        
        img1_png.save('../imgs/grayscale-test1.png')
        img2_png.save('../imgs/grayscale-test2.png')
        
    img1_out = img1.tolist()
    img2_out = img2.tolist()
    
    display_img1 = [[ reverse_bits(8*row[99:95:-1]), row[95:63:-1], row[63:31:-1],row[31::-1]] for row in img1_out]
    display_img2 = [[ reverse_bits(8*row[99:95:-1]), row[95:63:-1], row[63:31:-1],row[31::-1]] for row in img2_out]

    #then to int
    display_img1 = [[binary_list_to_int(word) for word in row] for row in display_img1]
    display_img2 = [[binary_list_to_int(word) for word in row] for row in display_img2]
    
    return [display_img1 , display_img2]
    

    

