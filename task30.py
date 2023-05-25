string = input("Введите строку: ")
counter = 0
counter1 = 0
for i in string:
 if i.lower() in "аеёиоуыэюя":
  counter += 1
 elif i.isalpha():
  counter1 += 1
print("Количество гласных букв:", counter)
print("Количество согласных букв:", counter1)
