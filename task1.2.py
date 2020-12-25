class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == "red":
            self.__color = "yellow"
            print("Светофор переключён на жёлтый. Продолжительность: 2 секунды")
        elif self.__color == "yellow":
            self.__color = "green"
            print("Светофор переключён на зелёный. Продолжительность: 7 секунд")
        elif self.__color == "green":
            self.__color = "red"
            print("Светофор переключён на красный. Продолжительность: 7 секунд")

    def running2(self, new_color):
        if self.__color == "red":
            if new_color != "yellow":
                print("Неправильный порядок переключения")
            else:
                self.__color = "yellow"
                print("Светофор переключён на жёлтый. Продолжительность: 2 секунды")
        elif self.__color == "yellow":
            if new_color != "green":
                print("Неправильный порядок переключения")
            else:
                self.__color = "green"
                print("Светофор переключён на зелёный. Продолжительность: 7 секунд")
        elif self.__color == "green":
            if new_color != "red":
                print("Неправильный порядок переключения")
            else:
                self.__color = "red"
                print("Светофор переключён на красный. Продолжительность: 7 секунд")


light = TrafficLight("green")
light.running()
light.running2("yellow")
light.running2("green")
light.running2("yellow")

