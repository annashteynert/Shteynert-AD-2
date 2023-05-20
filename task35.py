num = int(input("Введите количество : "))

result = [0, 1]

while len(result) < num:
 result.append(result[-1] + result[-2])

print(result)