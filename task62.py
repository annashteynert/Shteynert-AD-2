from math import sqrt

result = [(1,2),(3,4),(-1,5),(6,-3)]

sorted = sorted(result, key=lambda result: sqrt(result[0]**2 + result[1]**2), reverse=True)

print(sorted)