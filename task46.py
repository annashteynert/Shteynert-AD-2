import os

result = input('Введите имя файла: ')
if os.path.exists(result):
 try:
  with open(result, 'r') as file:
   print(file.read())
 except IOError:
  print('Error')
else:
 print('Error')


