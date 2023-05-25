from calculator import Calculator

calculator1 = Calculator()
num1=int(input('Введите число'))
num2=int(input('Введите число'))
print(calculator1.add(num1, num2))
print(calculator1.sub(num1, num2))
print(calculator1.multiply(num1, num2))
print(calculator1.divide(num1,num2))
