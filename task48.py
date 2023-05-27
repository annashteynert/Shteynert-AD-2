while True:
 try:
  x = int(input("Введите число: "))
  print(x ** 2)
  break
 except ValueError:
   print("Ошибка")