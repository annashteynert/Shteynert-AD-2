import random

arr = []

for i in range(10):
 arr.append(random.randint(1, 10))

print("Массив: ", arr)

sum_arr = sum(arr)


print("Сумма элементов массива: ", sum_arr)