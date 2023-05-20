number = int(input("Введите число: "))
arr = []

for i in range(2, number):
 if number % i == 0:
  arr.append(i)

if len(arr) == 0:
 print(number, "является простым числом")
else:
 print(number, "не является простым числом")