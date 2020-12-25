"""
 Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
 Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.
"""

import random

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость: {random.randint(0, int(self.speed))}")


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        speed = random.randint(0, self.speed)
        print(f"Скорость: {speed}")
        if speed > 60:
            print("Скорость превышена")


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        speed = random.randint(0, self.speed)
        print(f"Скорость: {speed}")
        if speed > 40:
            print("Скорость превышена")


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_a = Car(120, "Green", "Ford", False)
print(car_a.color)
car_a.show_speed()

car_b = WorkCar(120, "White", "Ford")
print(car_b.is_police)
car_b.show_speed()

car_c = TownCar(100, "Black", "Ford")
print(car_c.name)
car_c.show_speed()

car_d = PoliceCar(200, "White", "CopCar42")
print(car_d.is_police)
