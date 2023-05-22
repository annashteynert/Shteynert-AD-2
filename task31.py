class Calculator:
 def add(self, num1, num2):
  return num1 + num2

 def subtract(self, num1, num2):
  return num1 - num2

 def multiply(self, num1, num2):
  return num1 * num2

 def divide(self, num1, num2):
  return num1 / num2
calculator = Calculator()
num1=int(input('Введите число'))
num2=int(input('Введите число'))
print(calculator.add(num1, num2))
print(calculator.subtract(num1, num2))
print(calculator.multiply(num1, num2))
print(calculator.divide(num1, num2))
