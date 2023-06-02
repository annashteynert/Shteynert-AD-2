
try:
 x = float(input("Введите первое число: "))
 y = float(input("Введите второе число: "))
 if y == 0:
  raise ZeroDivisionError
 division = x / y
 print(division)
except ValueError:
 print("Error")
except ZeroDivisionError:
 print("Error")
