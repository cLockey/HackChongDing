# -*- coding: UTF-8 -*-  
  
from aip import AipOcr  
import json  
  
# 定义常量  
APP_ID = '10667663'  
API_KEY = 'O1CS9G7GKsNLbEPMfHg9iWuj'  
SECRET_KEY = 'iLqgzNORgIPmgdOerMwh4mDbBvGzl1ar'  

SCREENSHOT_PATH = 'screenshot/screen.png'

# 初始化AipFace对象  
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)  
  
# 读取图片  
def get_file_content(SCREENSHOT_PATH):  
    with open(SCREENSHOT_PATH, 'rb') as fp:  
        return fp.read()  
  
# 定义参数变量  
options = {  
  'detect_direction': 'true',  
  'language_type': 'CHN_ENG',  
}  
  
# 调用通用文字识别接口  
def ocr():
    result = aipOcr.basicGeneral(get_file_content(SCREENSHOT_PATH), options)  
    #print(json.dumps(result).decode.decode("unicode-escape"))  
    for k in result:
        print(k, result[k])

if __name__ == "__main__":  
    ocr()  