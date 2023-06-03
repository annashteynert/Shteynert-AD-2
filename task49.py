array = [5,7,11,13,15,20,25]
result = []
while array:
 num = array.pop()
 if num > 10:
  result.append(num)
result1 = sum(result)/len(result)
print(result1)
