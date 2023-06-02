import pathlib

result = pathlib.Path("my_folder")
if not result.exists():
 result.mkdir()
 print("result created")
else:
 print("result already exists")
