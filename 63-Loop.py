def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")   
    capitalized = phrase.capitalize()       
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)    
    else :
        return "{}.".format(capitalized)   


results = []
while True:
    user_input = input("Say somethine: ")          #要求用户输入信息
    if user_input =="\end":                        #如果输入的是end，则退出程序
        break
    else:
        results.append(sentence_maker(user_input))

print(results)
    