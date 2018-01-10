import cap_screen
import cut_image
import ocr

import time  

def hack():
    #cap_screen.screenshot()
    cut_image.cut_image()
    time1 = time.time()
    ocr.ocr()
    time2 = time.time()
    print(time2 - time1)

if __name__ == "__main__":
    hack()
