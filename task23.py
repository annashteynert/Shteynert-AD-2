import random
array = []

for i in range(10):
 array.append(random.randint(1, 10))


print("Массив: ", array)
number = int(input("Введите число: "))


if number in array:
 print("Число найдено в массиве")
else:
 print("Число не найдено в массиве")