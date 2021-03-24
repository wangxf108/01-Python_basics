myfile = open("fruits.txt")       #创建文件
content = myfile.read()
myfile.close()                    #关闭文件

print(content)                    #打印文件


with open("file.txt", "w") as file:        #答案
    file.write("snail")
    

    