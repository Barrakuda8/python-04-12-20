from sys import argv
from flinfunc import check


def fact(number):
    result = 1
    for i in range(1, number):
        result *= i
        yield result


if len(argv) != 2:
    print("Вы должны были ввести одно целое положительное число")
    exit()

n = check(argv[1], "Вы должны были ввести одно целое положительное число")

for el in fact(n):
    print(el)
