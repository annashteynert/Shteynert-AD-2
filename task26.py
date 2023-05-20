number1 = 11
number2 = 56


arr1 = []
arr2 = []


for i in range(1, number1 + 1):
 if number1 % i == 0:
  arr1.append(i)

for i in range(1, number2 + 1):
 if number2 % i == 0:
  arr2.append(i)


common_arr = []
for i in arr1:
  if i in arr2:
   common_arr.append(i)

print("Наименьший общий множитель чисел", number1, "и", number2, "равен", min(common_arr))