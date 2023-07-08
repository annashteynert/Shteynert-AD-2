class Student:
    def __init__(self, имя, возраст, средний_балл):
        self.имя = имя
        self.возраст = возраст
        self.средний_балл = средний_балл

students = [
    Student("Anna", 28, 4.3),
    Student("Valentina", 29, 1),
    Student("Nikita", 27, 5)
]

for student in students:
    print("Имя:", student.имя)
    print("Возраст:", student.возраст)
    print("Средний балл:", student.средний_балл)
    print()
