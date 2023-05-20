class Cooperator:
 def __init__(self, name, age, salary):
  self.name = name
  self.age = age
  self.salary = salary

 def information(self):
  print("Имя:", self.name)
  print("Возраст:", self.age)
  print("Зарплата:", self.salary)

cooperator1 = Cooperator("Никита", 20, 100000)
cooperator2 = Cooperator("Андрей", 33, 15000)
cooperator3 = Cooperator("Анна", 40, 330000)

cooperators = [cooperator1, cooperator2, cooperator3]

for cooperator in cooperators:
 cooperator.information()
print()