class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age

 def information(self):
  print(f"Имя: {self.name}, возраст: {self.age}")
person = Person("Валентина", 27)
person.information()
