# -*- coding: UTF-8 -*-  
from PIL import Image

SRC_SCREENSHOT_PATH = 'screenshot/src_screen.png'
DST_SCREENSHOT_PATH = 'screenshot/screen.png'

def cut_image():
    image = Image.open(SRC_SCREENSHOT_PATH)
    print("size: {}".format(image.size))
    src_width,src_height = image.size

    x = 0
    y = src_height / 5.5 
    new_width = src_width
    new_height = src_height * 0.45
    new_image = image.crop((x, y, x+new_width, y+new_height))
    new_image.save(DST_SCREENSHOT_PATH)

if __name__ == "__main__":  
    cut_image()  