def mean(*args):                  # (*args) 指代参数，具有普遍通用性，常用
    return sum(args) / len(args)

print(mean(1, 3, 4))