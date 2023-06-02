
try:
 x = float(input("Введите первое число: "))
 y = float(input("Введите второе число: "))
 if y == 0:
  raise ZeroDivisionError
 result = x / y
 print(result)
except ValueError:
 print("Error")
except ZeroDivisionError:
 print("Error")
