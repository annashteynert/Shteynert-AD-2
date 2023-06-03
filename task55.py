number = input("Введите целое число N: ")
try:
 number = int(number)
 if number < 1:
  print("")
 else:
  result = list(range(1, number+1))
  result.reverse()
  summ = sum(result)
  print(summ)
except ValueError:
  print("error")