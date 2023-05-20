num = input("Введите два числа и операцию через пробел: ").split()
num1 = float(num[0])
num2 = float(num[1])
operation = num[2]

if operation == "+":
 esult = num1 + num2
elif operation == "-":
result = num1 - num2
elif operation == "*":
result = num1 * num2
elif operation == "/":
if num2 == 0:
print("Ошибка! Деление на ноль невозможно.")
else:
result = num1 / num2
else:
print("Ошибка! Неверная операция.")

if "result" in locals():
print("Результат:", result)