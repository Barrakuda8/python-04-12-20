from sys import argv
from flinfunc import check


def salary(per_h, h, b=0.0):
    return per_h * h + b


if len(argv) != 3 and len(argv) != 4:
    print("Требовалось ввести ставку в час, количество часов и возможную премию")
    exit()

money = check(argv[1], "Ставка в час должна быть положительным часлом", float)
hours = check(argv[2], "Количество часов должно быть положительным числом", float)
bonus = check(argv[3], "Премия должна быть положительным числом", float)

print(f"Ваша зарплата составит: {round(salary(money, hours, bonus), 2)}")


