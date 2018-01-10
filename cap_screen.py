#!/usr/bin/env python  
  
import os  
import time  

PATH = lambda p: os.path.abspath(p)  
SCREENSHOT_NAME = "src_screen"

def screenshot():  
    path = PATH(os.getcwd() + "/screenshot")  
    #timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))  
    adbPath = PATH(os.getcwd() + "/adb/")
    
    os.popen(adbPath + "\\adb wait-for-device")  
    os.popen(adbPath + "\\adb shell screencap -p /data/local/tmp/tmp.png")  
    if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):  
        os.makedirs(path)  
    
    os.popen(adbPath + "\\adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + SCREENSHOT_NAME + ".png"))  
    os.popen(adbPath + "\\adb shell rm /data/local/tmp/tmp.png")  
    print ('success')
  
if __name__ == "__main__":  
    screenshot()  