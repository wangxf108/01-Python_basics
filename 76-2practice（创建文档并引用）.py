#生成文档，并引入其他文档内容
with open("bear.txt") as file:              #引用已知文档
    content = file.read()                   #引用已知文档内容

with open("first.txt", "w") as file:        #创建新的文档
    file.write(content[:90])                #将引用文档的前90内容引入创建文档中
    