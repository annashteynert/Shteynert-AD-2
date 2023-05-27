import os

directory = 'my_folder'
if not os.path.exists(directory):
  try:
   os.mkdir(directory)
   print(f"Создание  '{directory}' прошло успешно ")
  except OSError:
   print(f"Директория '{directory}' не создана")
else:
   print(f"Директория '{directory}' уже есть")
