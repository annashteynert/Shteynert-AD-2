N = [5, 1, 10, 3, 7]
N.sort()
result = tuple(N.pop(0) for i in range(len(N)))
print(result)