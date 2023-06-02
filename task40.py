
import pathlib

result = pathlib.Path("text.txt")
if result.exists():
 print("file exists")
else:
 print("file not found")
