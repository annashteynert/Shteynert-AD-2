import os

if os.path.exists('text.txt'):
 with open('text.txt', 'r') as result:
    print(result.read())
else:
    print('file not found')
