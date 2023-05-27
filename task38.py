try:
 file = open("text.txt", "r")
 text = file.readlines()
 for i in text:
  print(i.strip())
 file.close()
except FileNotFoundError:
    print("Файл не найден")
