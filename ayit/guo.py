import cv2
import numpy as np 
import matplotlib.pyplot as plt

def  flipupdown(image):
    height,width,channels = image.shape
    image_flipped = image.copy()
    image_flipped[::-1,0:width] = image[0:height,0:width]    
    return image_flipped 
def flip_left_right(image):
    image_flipped = image.copy()
    height,width,channels =image.shape
    image_flipped[0:height,::-1] = image[0:height,0:width]
    return image_flipped 

def flip_digonal(image):
    image_flipped = image.copy()
    height,width,channels =image.shape
    image_flipped = flipupdown(flip_left_right(image))
    return image_flipped 










