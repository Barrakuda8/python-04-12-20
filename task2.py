class ZeroDivError(Exception):

    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def valid_division(cls, dividend):
        if dividend == 0:
            raise ZeroDivError("Нельзя делить на 0")
        return dividend


try:
    print(float(input("Введите делимое: ")) / ZeroDivError.valid_division(float(input("Введите делитель: "))))
except ValueError:
    print("Вы должны были ввести числа")
except ZeroDivError as ZDE:
    print(ZDE.txt)
