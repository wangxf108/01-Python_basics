temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]  #排除干扰项
print(new_temps)

new_temps = [temp / 10 for temp != -9999 else 0 for temp in temps]   #此时，如果等于-9999则输出0