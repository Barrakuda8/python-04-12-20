import time


class TrafficLight:
    __color = "green"

    def running(self):
        __color = "red"
        print(__color)
        time.sleep(7)
        __color = "yellow"
        print(__color)
        time.sleep(2)
        __color = "green"
        print(__color)
        time.sleep(7)


light = TrafficLight()
light.running()

