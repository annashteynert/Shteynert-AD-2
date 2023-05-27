import os

try:
 os.mkdir("my_folder")
 print("Директория создана")
except FileExistsError:
 print("Директория уже существует")