
import os

if os.access("text.txt", os.F_OK):
 print("Файл существует")
else:
 print("Файл не найден")