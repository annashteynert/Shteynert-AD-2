array = [1, 2, 3, 2, 1]
result = True

for i in range(len(array)):
 if array[i] != array[-i-1]:
  result = False
  break

if result:
 print("палиндром")
else:
 print(" не является палиндромом")