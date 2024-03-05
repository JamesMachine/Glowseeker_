from PIL import Image, ImageDraw 
import numpy as np


def reshape_circle(h, w):

    img = Image.open("img01.png")
    lum_img = Image.new('L',[h,w] ,0)  
    draw = ImageDraw.Draw(lum_img) 
    draw.pieslice([(0,0),(h,w)],0,360,fill=255) 
    img_arr = np.array(img) 
    lum_img_arr = np.array(lum_img) 
    
    return lum_img_arr
    
    # display(Image.fromarray(lum_img_arr))
