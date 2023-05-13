class Cat:
 def __init__(self, name, age, color):
  self.name = name
  self.age = age
  self.color = color

 def info(self):
  print(f"Кошка по имени {self.name}, {self.age} лет, цвет {self.color}")
cat = Cat("Мурка", 7, "рыжий")
cat.info()