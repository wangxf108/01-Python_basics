import time                                           #导入 time module模块
import os                                             #导入 os module模块

while True:                     
    if os.path.exists("files/vegetables.txt"):        #如果在路径下vegetables文件存在
        with open("files/vegetables.txt") as file:    
            print(file.read())                        #读入文件
    else:                           
        print("File dose not exist.")
    time.sleep(10)                                    #程序的循环实践是10秒钟一次