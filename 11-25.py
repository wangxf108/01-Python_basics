# 挺多不会的，主要是根本不知道，还有就是基础的数据类型，各种括号，双引号。要记住。

# # 注意，两个井号的例子，是自己比较不擅长的。


#12 两种方法获得一个10，20，。。200的列表
# my_range = range(10,210,10)
# print(list(my_range))

# my_range = range(1,21)
# print([10 * i for i in my_range])

##13 输出1到21的字符串形式，将str放在my_range前面，定义输出类型。
# my_range = range(1, 21)
# print(list(map(str, my_range)))

## 14.We used a set  function to convert the list to a set that would intermediately produce {'1', 1, 2}  with no duplicates because set objects cannot contain duplicates. Then using list  we converted the set back to a list. The drawback here is that the original order of the items is lost. If you need to preserve the order, you may want to use the solution in Answer 2 below.
# answer1:
# a = ["1", 1, "1", 2]
# a = list(set(a)) 
# print(a)
# answer2:
# a = ["1", 1, "1", 2]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

## 15 定义一个字典类型的两种方式
# c = {"a" : 1, "b": 2}
# c = dict(a = 1, b = 2)

# c = {"a" : 1, "b" : 2}
# c = dict(a = 1, b = 2)

# d = {"a":1 , "b":2}
# d = dict(a = 1, b = 2)

# 16.打印出对应的key的数值，自己的方法会打印出全部的key
# d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6}
# for value in d.items():
#     print(value[1])

# 打印出字典出对应的key值
# d = {"a": 1, "b": 2}
# print(d["b"])

# 17Question: Calculate the sum of the values of keys a  and b .
# d = {"a": 1, "b": 2, "c": 3}
# print (d["a"] + d["b"])


# 18 print out smith
# d = {"Name": "John", "Surname": "Smith"}
# print(d["Surname"])

# 19.Add a new pare of key and value to the dictionary
# # 在字典中加入新的key值，方法很直接。直接添加，打印就可以。
# d = {"a":1, "b":2}
# d["c"] = 3
# print(d)


# 20Calculate the sum of all dictionary values.
# d = {"a": 1, "b": 2, "c": 3}
# e = sum(d.values())
# print(e)
# print(sum(d.values()))

## 21 Filter the dictionary by removing all items with a value of greater than 1.
# d = {"a": 1, "b": 2, "c": 3}
# d = dict((key, value) for key, value in d.items() if value <=1)
# print(d)

# 22.Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30, respectively. 
# Then print out the dictionary in a nice format.
# from pprint import pprint
# d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
# pprint(d)

# 23 访问b的第三个数
# from pprint import pprint
# d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
# pprint(d["b"][2])

# 24.插入话语段落
# from pprint import pprint
# d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
# for key, value in d.items():
#     print(key, "has value", value)

# 25.print out the alphebt from a to z
# import string 
# for letter in string.ascii_lowercase:
#     print(letter)
