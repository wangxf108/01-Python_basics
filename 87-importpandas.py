import time                                       
import os                                        
import pandas

while True:                     
    if os.path.exists("files/temps_today.csv"):       
        data = pandas.read_csv("files/temps_today.csv")     #运用pandas读取csv文件中的数据  
        print(data.mean()["st1"])                           #只读取一个station的数据，如果全读出，则删除【“st1”】
    else:                           
        print("File dose not exist.")
    time.sleep(10)                     