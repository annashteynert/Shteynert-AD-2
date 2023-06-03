import os
import copy

class TodoList:
 def __init__(self):
  self.file_path = "todo_list.txt"
  if os.path.exists(self.file_path):
   with open(self.file_path, "r") as f:
    self.items = f.read().splitlines()
  else:
    self.items = []

def add_item(self, item):
 self.items.append(item)
 self._save_to_file()

def remove_item(self, item):
 if item in self.items:
   self.items.remove(item)
   self._save_to_file()

def display_list(self):
 print("Todo List:")
 for item in self.items:
  print("- " + item)

def _save_to_file(self):
 with open(self.file_path, "w") as f:
  f.write("\n".join(self.items))


my_list = TodoList()
my_list.add_item("купить цветы")
my_list.add_item("помыть посуду")
my_list.display_list()
my_list.remove_item("сходить на работу")
my_list.display_list()