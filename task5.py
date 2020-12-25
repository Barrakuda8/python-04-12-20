class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки маркером")


stat_a = Stationery("Штука")
stat_a.draw()
pen_a = Pen("Ручка")
pen_a.draw()
pencil_a = Pencil("Карандаш")
pencil_a.draw()
handle_a = Handle("Маркер")
handle_a.draw()