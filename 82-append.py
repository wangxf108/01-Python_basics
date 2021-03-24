with open("files/fruits.txt", "a+") as myfile:      #创建文档，此处“a”是append，附录；“+”可以保证同时进行读，写
    myfile.write("\n0kra")                          #加入新文档（此时光标在尾端） "\n"换行
    myfile.seek(0)                                  #让光标回到第一行，为了可以将所有内容都打印出来
    content = myfile.read()                         #记录出文档中所有内容

print(content)                                      #打印出出文档中所有内容