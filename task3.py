class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            print("Невозможно выполнить вычитание")

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        # этого в задании нет, но мне кажется, что тут как с вычитанием по сути
        if self.quantity / other.quantity > 0:
            return Cell(self.quantity // other.quantity)
        else:
            print("При целочисленном делении будет 0 ячеек")

    def make_order(self, row):
        result = ""
        for n in range(self.quantity // row):
            result += row * "*" + "\n"
        return result + (self.quantity % row) * "*"


cell_a = Cell(20)
cell_b = Cell(30)
cell_c = Cell(40)

assert (cell_a + cell_b).quantity == 50
assert (cell_c - cell_b).quantity == 10
assert cell_b - cell_c is None
assert (cell_a * cell_b).quantity == 600
assert (cell_c / cell_a).quantity == 2
assert (cell_c / cell_b).quantity == 1
print(cell_a.make_order(3))
