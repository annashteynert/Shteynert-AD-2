class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def result(self):
        return self.length * self.width
geometricfigure = Rectangle(60, 70)
print(geometricfigure.result())
