with open("fruits.txt") as myfile:          #导入文件的另一种方式，能够让程序更加有 条理
    content = myfile.read()

print(content)

file = open("bear.txt")
content = file.read()
file.close()
print(content[:90])