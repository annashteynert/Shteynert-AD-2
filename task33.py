string = input("Введите строку: ")
num = {}

for i in string:
 num[i] = num.get(i, 0) + 1

for i, counter in num.items():
 print("Символ '{}' встречается {} раз(а).".format(i, counter))