import time


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self, new_color):
        col = {"red": ("yellow", 2), "yellow": ("green", 7), "green": ("red", 7)}
        if new_color != col[self.__color][0]:
            print("Неправильный порядок переключения")
        else:
            print(f"Светофор переключён на {col[self.__color][0]}. Продолжительность: {col[self.__color][1]} сек")
            time.sleep(col[self.__color][1])
            self.__color = new_color


light = TrafficLight("red")
light.running("yellow")
light.running("green")
light.running("red")
light.running("green")
