while True:
 try:
  x = float(input("Введите первое число: "))
  y = float(input("Введите второе число: "))
  division = x / y
  print(division)
  break
 except ValueError:
  print("Ошибка")
 except ZeroDivisionError:
  print("Ошибка")
  break
