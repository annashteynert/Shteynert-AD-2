class Student:
 def __init__(self, name, surname, course, estimates):
  self.name = name
  self.surname = surname
  self.course = course
  self.estimates = estimates

 def average_estimate(self):
  return sum(self.estimates) / len(self.estimates)
estimates = [5, 5, 5, 5, 2]
student = Student("Иван", "Иванов", 2, estimates)
print(f"Средний балл студента {student.name} {student.surname} на курсе {student.course}: {student.average_estimate()}")
