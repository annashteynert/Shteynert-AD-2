class calculator1:
 def func1(self, num1, num2):
  return num1 + num2

 def func2(self, num1, num2):
  return num1 - num2

 def func3(self, num1, num2):
  return num1 * num2

 def func4(self, num1, num2):
  return num1 / num2
calculator = calculator1()
num1=int(input('Введите число'))
num2=int(input('Введите число'))
print(calculator.func1(num1, num2))
print(calculator.func2(num1, num2))
print(calculator.func3(num1, num2))
print(calculator.func4(num1, num2))
