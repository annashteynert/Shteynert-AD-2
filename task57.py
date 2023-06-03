try:
 file1 = input(" ")
 with open(file1, "r") as file:
  words = file.read().split()
  result = [word[::-1] for word in words]
  result1= max(set(result), key=result.count)
  often_word = result1[::-1]
  print(often_word)
except FileNotFoundError:
  print("error")