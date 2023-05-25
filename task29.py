def reverse_str(result):
 if len(result) == 0:
  return result
 else:
  return reverse_str(result[1:]) + result[0]
string1 = input("Введите строку: ")
reversed_str = reverse_str(string1)
print("Результат:", reversed_str)
