import os

info = input('название файла:')
if os.path.exists(info):
 try:
  with open(info, 'r') as file:
   print(file.read())
 except Exception as file1:
   print(f"Ошибка: {file1}")
else:
 print("Файл не существует")



