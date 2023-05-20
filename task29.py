number = input("Введите числа: ").split()
number1 = float(number[0])
number2 = float(number[1])
operation = number[2]

if operation == "+":
 number3 = number1 + number2
elif operation == "-":
 number3 = number1 - number2
elif operation == "*":
 number3 = number1 * number2
elif operation == "/":
 if number2 == 0:
  print("делить на ноль нельзя.")
 else:
  number3 = number1 / number2
else:
  print("операция невозможна.")

if "number3" in locals():
 print("Результат:", number3)