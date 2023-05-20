import random

arr = []

for i in range(10):
 number = random.randint(1, 100)
 arr.append(number)

print("Массив: ", arr)

max_num = max(arr)
min_num = min(arr)

print("Максимальное число: ", max_num)
print("Минимальное число: ", min_num)