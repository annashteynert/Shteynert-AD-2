import os

try:
  dir = input(" ")
  num = input(" ")
  files = []
  for root, dirs, files1 in os.walk(dir):
   files.extend([os.path.join(root, filename) for filename in files1 if filename.endswith(num)])
  files.sort()
  print(f"Найдено {len(files)} с {num} в директории {dir} :")
  for i in files:
    print(i)
except FileNotFoundError:
    print("Ошибка")