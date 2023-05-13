class Dog:
 def __init__(self, name, breed, age):
  self.name = name
  self.breed = breed
  self.age = age

 def information(self):
  print(f"Имя: {self.name}, порода: {self.breed}, возраст: {self.age}")
animal = Dog("Дружок", "лабрадор", 5)
animal.information()