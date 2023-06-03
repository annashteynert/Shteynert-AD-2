N = input(" ")
list_of_numbers = N.split(",")
try:
 list_of_numbers = [int(num) for num in list_of_numbers]
 min = list_of_numbers.pop()
 while list_of_numbers:
  num = list_of_numbers.pop()
  if num < min:
   min = num
  print(f"Минимальное число: {min}")
except ValueError:
  print("Ошибка")
