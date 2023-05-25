def reverse_str(string):
 string_list = list(string)
 string_list.reverse()
 return ''.join(string_list)
string1 = input("Введите строку: ")
reversed_str = reverse_str(string1)
print("Результат:", reversed_str)
