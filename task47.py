try:
 with open('text.txt', 'w') as line:
   line.write('Hello, world!')
except Exception:
 print("Ошибка")