result = None
try:
 result = int(input('Введите число: '))
 print(result**2)
except:
 print('Error')
finally:
 if result is not None:
  del result
