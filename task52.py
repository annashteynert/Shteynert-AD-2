first_arrray = [24, 36, 48, 60]
second_array = [12, 18, 24, 36, 72]

def gcd(num1, num2):
 while num2 != 0:
  num1, num2 = num2, num1 % num2
  return num1


def gcd_arr(arr):
 result = arr[0]
 for i in range(1, len(arr)):
  result = gcd(result, arr[i])
  return result


result = first_arrray + second_array

result.sort()


result = gcd_arr(result)

print(result)