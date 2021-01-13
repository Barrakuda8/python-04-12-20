from random import randint, choice
from string import ascii_uppercase
import typing


class Warehouse:

    def __init__(self, data: dict):
        self.data = data

    def add_item(self, equipment: str, item: OfficeEquipment()):
        self.data[equipment.lower()].append(item)

    def transport_by_sn(self, other, equipment, serial_num):
        equipment = equipment.lower()
        if equipment not in self.data:
            print("На этом складе нет этого товара")
        else:
            for i in range(len(self.data[equipment])):
                if self.data[equipment][i].serial_num == serial_num:
                    if equipment not in other.data:
                        other.data[equipment] = []
                    other.data[equipment].append(self.data[equipment][i].pop(i))

    def transport_by_quantity(self, other, equipment, quantity: int, **kwargs):
        equipment = equipment.lower()
        if equipment not in self.data:
            print("На этом складе нет этого товара")
        elif len(self.data[equipment]) < quantity:
            print(f"Недостаточно единиц товара: {len(self.data[equipment])}")
        else:
            to_transport = []
            for i in range(self.data[equipment]):
                if len(to_transport) == quantity:
                    break
                for key, value in kwargs:
                    n = 0
                    if self.data[equipment][i].key == value:
                        n += 1
                    elif n == len(kwargs):
                        to_transport.append(self.data[equipment][i].pop())
                    else:
                        break
            if len(to_transport) <= quantity:
                answer = input(f"Недостаточно единиц подходящего товара: {len(to_transport)}\n"
                               f"Перевезти имеющееся количество подходящего товара? ('Да' или 'Нет')\n>>> ")
                while True:
                    if answer.lower() == "да":
                        to_transport.extend(other.data[equipment])
                        break
                    elif answer.lower() == "нет":
                        to_transport.extend(self.data[equipment])
                    else:
                        answer = input("Введите 'Да' или 'Нет'\n>>> ")
            else:
                to_transport.extend(other.data[equipment])


class OfficeEquipment:

    def __init__(self, serial_num, model, year, warranty, color):
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


class Scanner(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color):
        super().__init__(serial_num, model, year, warranty, color)


class CopyMachine(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color):
        super().__init__(serial_num, model, year, warranty, color)


warehouse_a = Warehouse({})
warehouse_b = Warehouse({"printer": [Printer.generate(), Printer.generate(), Printer.generate()]})
print(warehouse_b.data["printer"][0].serial_num, warehouse_b.data["printer"][0].model,
      warehouse_b.data["printer"][0].color, warehouse_b.data["printer"][0].warranty,
      warehouse_b.data["printer"][0].year)
warehouse_b.transport_by_quantity(warehouse_a, "printer", 2)
print(warehouse_b.data, warehouse_a.data)
warehouse_b.transport_by_quantity(warehouse_a, "printer", 2)
print(warehouse_b.data, warehouse_a.data)
warehouse_b.transport_by_quantity(warehouse_a, "scanner", 2)
print(warehouse_b.data, warehouse_a.data)

