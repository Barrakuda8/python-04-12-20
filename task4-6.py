from random import randint, choice
from string import ascii_uppercase
import inspect


class Warehouse:

    def __init__(self, name, data: dict):
        self.name = name
        self.data = data

    def __str__(self):
        return self.name

    def add_item(self, equipment: str, item: 'OfficeEquipment'):
        if equipment.lower() not in self.data:
            self.data[equipment.lower()] = []
        self.data[equipment.lower()].append(item)

    def transport_by_sn(self, other, equipment: str, serial_num: str):
        equipment = equipment.lower()
        if equipment not in self.data:
            print("На этом складе нет этого товара")
        else:
            for i in range(len(self.data[equipment])):
                if self.data[equipment][i].serial_num == serial_num:
                    if equipment not in other.data:
                        other.data[equipment] = []
                    other.data[equipment].append(self.data[equipment][i])
                    del (self.data[equipment][i])

    @staticmethod
    def get_random_name():
        return f"Cowabunga{randint(1000, 9999)}"


class OfficeEquipment:

    def __init__(self, serial_num: str, model: str, year: int, warranty: int, color: str):
        self.serial_num = serial_num
        self.model = model
        self.year = year
        self.warranty = warranty
        self.color = color

    @staticmethod
    def generate_serial_num():
        return f"{randint(1000, 9999)}-{''.join(choice(ascii_uppercase) for _ in range(4))}-{randint(1000, 9999)}"

    @staticmethod
    def generate_model():
        return f"{choice(ascii_uppercase)}"

    @staticmethod
    def generate_year():
        return randint(2015, 2020)

    @staticmethod
    def generate_warranty():
        return randint(1, 5)

    @staticmethod
    def generate_color():
        return choice(["black", "white", "grey"])

    @classmethod
    def generate(cls):
        return cls(cls.generate_serial_num(), cls.generate_model(), cls.generate_year(),
                   cls.generate_warranty(), cls.generate_color())


class Printer(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color, bw_or_color):
        super().__init__(serial_num, model, year, warranty, color)
        self.bw_or_color = bw_or_color

    @staticmethod
    def generate_bw_or_color():
        return choice(["bw", "color"])

    @classmethod
    def generate(cls):
        return cls(cls.generate_serial_num(), cls.generate_model(), cls.generate_year(),
                   cls.generate_warranty(), cls.generate_color(), cls.generate_bw_or_color())

    @staticmethod
    def check_bw_or_color(data):
        if data == "bw" or data == "color":
            return data
        else:
            raise ValueError


class Scanner(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color):
        super().__init__(serial_num, model, year, warranty, color)


class CopyMachine(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color):
        super().__init__(serial_num, model, year, warranty, color)


class Menu:

    def __init__(self, *args):
        self.options = list(args)

    def __str__(self):
        to_print = ""
        for i in self.options:
            to_print = "".join([to_print, f'{i}\n'])
        return to_print

    @classmethod
    def create_warehouse_menu(cls, warehouse: 'Warehouse'):
        warehouse_items = []
        for key, value in warehouse.data.items():
            values = ""
            for i in range(len(value)):
                if not values:
                    values = "".join([values, f"({i + 1}).({value[i].serial_num})"])
                else:
                    values = ", ".join([values, f"({i + 1}).({value[i].serial_num})"])
            warehouse_items.append(f"({len(warehouse_items) + 1}){key}: {values}")
        return cls(f"Склад {warehouse}", "-Добавить товар: 1", "-Перевезти товар по серийному номеру: 2",
                   "-Удалить товар по серийному номеру: 3",
                   "-Чтобы посмотреть товар, введите его порядковый номер по образцу 4.x.y\n"
                   " К примеру: 4.1.1 - первый товар первого типа", "-На главную: 0",
                   *warehouse_items)

    @classmethod
    def create_equipment_menu(cls, equipment: 'OfficeEquipment'):
        eq_attrs = []
        for i in inspect.getmembers(equipment):
            if not i[0].startswith('_') and not inspect.ismethod(i[1]) and not inspect.isfunction(i[1]):
                eq_attrs.append(f"{i[0]}: {i[1]}")
        return cls(*eq_attrs, "-Назад: 0")

    def get_answer(self, answers: list):
        print(self)
        while True:
            answer = input(">>> ")
            if answer.lower() not in answers:
                print("Недопустимый ввод")
                continue
            else:
                return answer


class UI:

    @staticmethod
    def user_input(txt, func):
        while True:
            answer = input(f"Введите {txt}\n>>> ")
            if answer == "":
                return answer
            try:
                return func(answer)
            except ValueError:
                print("Недопустимый ввод")
                continue

    def get_warehouse(self, txt, warehouse: 'Warehouse'):
        while True:
            answer = input(f"{txt}\n>>> ")
            if answer == "here":
                return warehouse
            else:
                for wh in self.warehouses:
                    if answer in wh.name:
                        return wh
                print("Такого склада не существует")

    def __init__(self):
        self.main_menu = Menu("-Создать склад: 1", "-Посмотреть склады: 2")
        self.warehouse_list = Menu("-Назад: 0", "-Посмотреть склад: порядковый номер склада")
        self.warehouses = []
        self.main_menu_method()

    def main_menu_method(self):
        answer = self.main_menu.get_answer(["1", "2"])
        if answer == "1":
            self.create_warehouse()
        elif answer == "2":
            self.warehouse_list_method()

    def warehouse_list_method(self):
        if len(self.warehouses) == 0:
            print("Пока не создано ни одного склада")
        answers = ["0"]
        for i in range(len(self.warehouses)):
            answers.append(f"{i + 1}")
        answer = self.warehouse_list.get_answer(answers)
        if answer == "0":
            self.main_menu_method()
        else:
            self.warehouse_menu_method(self.warehouses[int(answer) - 1])

    def warehouse_menu_method(self, warehouse: 'Warehouse'):
        menu = Menu.create_warehouse_menu(warehouse)
        answers = ["0", "1", "2", "3"]
        i = 0
        for key in warehouse.data.keys():
            i += 1
            for j in range(len(warehouse.data[key])):
                answers.append(f"4.{i}.{j+1}")
        answer = menu.get_answer(answers)
        if answer == "0":
            self.main_menu_method()
        elif answer == "1":
            self.create_equipment(warehouse)
        elif answer == "2":
            self.transport_by_ser_num(warehouse)
        elif answer == "3":
            self.delete_equipment(warehouse)
        else:
            cords = list(map(int, answer.split(".")))
            self.equipment_menu_method(warehouse.data[list(warehouse.data)[cords[1] - 1]][cords[2] - 1], warehouse)

    def equipment_menu_method(self, equipment: 'OfficeEquipment', back: 'Warehouse'):
        menu = Menu.create_equipment_menu(equipment)
        menu.get_answer(["0"])
        self.warehouse_menu_method(back)

    def create_warehouse(self):
        name = self.user_input("название склада", str)
        if name == "":
            name = Warehouse.get_random_name()
        for warehouse in self.warehouses:
            if warehouse.name == name:
                print("Склад с таким названием уже существует")
                self.create_warehouse()
        warehouse = Warehouse(name, {})
        self.warehouses.append(warehouse)
        self.warehouse_list.options.append(f"({len(self.warehouses)}).{warehouse.name}")
        self.warehouse_menu_method(warehouse)

    def create_equipment(self, warehouse: 'Warehouse'):
        attrs_type = {"serial_num": str, "model": str, "year": int, "warranty": int, "color": str}
        answer = Menu("Какой вид товара вы хотите добавить?\n"
                      "Доступные товары: printer, scanner, copy machine\n"
                      "Для создания товара со случайными характеристиками, добавьте 'r' через пробел"
                      ).get_answer(["printer", "scanner", "copy machine", "printer r", "scanner r", "copy machine r"])
        answer = "".join(list(map(lambda x: x.title(), answer.split())))
        if answer[-1] == "R":
            warehouse.add_item(answer[:-1], eval(answer[:-1]).generate())
        else:
            equipment = eval(answer).generate()
            eq_attrs = {}
            for i in inspect.getmembers(equipment):
                if not i[0].startswith('_') and not inspect.ismethod(i[1]) and not inspect.isfunction(i[1]):
                    if i[0] == "bw_or_color":
                        eq_attrs[i[0]] = self.user_input(f"{i[0]}", Printer.check_bw_or_color)
                        if eq_attrs[i[0]] == "":
                            eq_attrs[i[0]] = equipment.generate_bw_or_color()
                    else:
                        eq_attrs[i[0]] = self.user_input(f"{i[0]}", attrs_type[i[0]])
                        if eq_attrs[i[0]] == "":
                            eq_attrs[i[0]] = eval(f"equipment.generate_{i[0]}()")
            warehouse.add_item(answer, eval(answer)(**eq_attrs))
        self.warehouse_menu_method(warehouse)

    def transport_by_ser_num(self, warehouse: 'Warehouse'):
        start = self.get_warehouse("Откуда? (Напишите 'here' для назначения этого склада или введите имя склада",
                                   warehouse)
        finish = self.get_warehouse("Куда? (Напишите 'here' для назначения этого склада или введите имя склада",
                                    warehouse)
        while True:
            equipment = "".join(input("Какой вид товара вы хотите перевезти?\n>>> ").split()).lower()
            if equipment not in start.data:
                print("На этом складе нет такого товара")
                continue
            else:
                break
        n = 0
        while n != 1:
            serial_num = input("Введите серийный номер товара\n>>> ")
            for item in start.data[equipment]:
                if serial_num == item.serial_num:
                    n = 1
                    break
            if n == 0:
                print("Товара этого вида с таким серийным номером нет на складе")
        start.transport_by_sn(finish, equipment, serial_num)
        if not start.data[equipment]:
            del start.data[equipment]
        self.warehouse_menu_method(finish)

    def delete_equipment(self, warehouse: 'Warehouse'):
        n = 0
        while n != 1:
            serial_num = input("Введите серийный номер товара\n>>> ")
            for key, value in warehouse.data.items():
                for i in value:
                    if serial_num == i.serial_num:
                        value.remove(i)
                        n = 1
                        break
                if not warehouse.data[key]:
                    del warehouse.data[key]
                    break
            if n == 0:
                print("Товара этого вида с таким серийным номером нет на складе")
        self.warehouse_menu_method(warehouse)


ui = UI()