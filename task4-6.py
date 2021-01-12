from random import randint, choice
import re

class Warehouse:

    def __init__(self, data: dict):
        self.data = data

    def add_item(self, equipment, item):
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

    def transport_by_quantity(self, other, equipment, quantity: int):
        equipment = equipment.lower()
        if equipment not in self.data:
            print("На этом складе нет этого товара")
        else:
            if len(self.data[equipment]) <= quantity:
                print(f"Недостаточно товара. Всего на этом складе осталось единиц товара: {len(self.data[equipment])}")
            else:
                if equipment not in other.data:
                    other.data[equipment] = []
                for i in range(quantity):
                    other.data[equipment].append(self.data[equipment].pop(i))


class OfficeEquipment:

    def __init__(self, serial_num, model, year, warranty, color):
        self.serial_num = serial_num
        self.model = model
        self.year = year
        self.warranty = warranty
        self.color = color

    @classmethod
    def generate(cls):
        serial_num = f"{randint(1000, 9999)}-{choice(r'[A-Z]{4}')}-{randint(1000, 9999)}"
        model = f"{choice(r'[A-Z]')}"
        year = randint(2015, 2020)
        warranty = randint(1, 5)
        color = choice(["black", "white", "grey"])
        return cls(serial_num, model, year, warranty, color)


class Printer(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color):
        super().__init__(serial_num, model, year, warranty, color)


class Scanner(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color):
        super().__init__(serial_num, model, year, warranty, color)


class CopyMachine(OfficeEquipment):

    def __init__(self, serial_num, model, year, warranty, color):
        super().__init__(serial_num, model, year, warranty, color)


warehouse_a = Warehouse({})
warehouse_b = Warehouse({"printer": [Printer.generate(), Printer.generate(), Printer.generate()]})
print(warehouse_b.data["printer"][0].serial_num)
warehouse_b.transport_by_quantity(warehouse_a, "printer", 2)
print(warehouse_b.data, warehouse_a.data)
warehouse_b.transport_by_quantity(warehouse_a, "printer", 2)
print(warehouse_b.data, warehouse_a.data)
warehouse_b.transport_by_quantity(warehouse_a, "scanner", 2)
print(warehouse_b.data, warehouse_a.data)

