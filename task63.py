class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def result(self, seconds):
        kilometres = self.speed * seconds
        print(f"{self.name} проехал {kilometres} метров за {seconds} секунд")

class Robot1(Robot):
    def __init__(self, name, speed, zone):
        super().__init__(name, speed)
        self.zone = zone

class Robot2(Robot):
    def __init__(self, name, speed, make):
        super().__init__(name, speed)
        self.make = make

robot1 = Robot("Робот ", 10)
robot2 = Robot1("Гусеничный робот", 20, "Скорпион")
robot3 = Robot2("Робот на колесах", 30, "Toyota")

robots = [robot1, robot2, robot3]
robots.sort(key=lambda x: x.speed)

for robot in robots:
    robot.result(10)