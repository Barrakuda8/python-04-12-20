class Complex:

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"{self.i} + {self.j}j"

    def __add__(self, other):
        return Complex(self.i + other.i, self.j + other.j)

    def __mul__(self, other):
        return Complex(self.i * other.i - self.j * other.j, self.i * other.j + other.i * self.j)


comp_a = Complex(4, 1)
comp_b = Complex(5, 4)
print(comp_a + comp_b)
print(comp_a * comp_b)
