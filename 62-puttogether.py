def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")   #疑问句
    capitalized = phrase.capitalize()         #将phrase的首字母大写
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)      #如果是疑问句，就加问号，并大写首字母
    else :
        return "{}.".format(capitalized)      #非疑问句，就加句号，并大写首字母

print(sentence_maker("how are you"))