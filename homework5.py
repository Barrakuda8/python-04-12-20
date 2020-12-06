# хотелось бы знать есть ли аналог метода isdigit() для float, я к сожалению не нашёл
revenues = float(input("Введите выручку фирмы\n >>>"))
costs = float(input("Введите издержки фирмы\n >>>"))

result = revenues - costs

if result < 0:
    print("Убыток вашей фирмы составляет", result)
    exit()
elif result == 0:
    print("Ваша фирма работает в 0")
    exit()
else:
    print("Прыбыль вашей фирмы составляет", result)

print("Рентабельность выручки равна", round(result / revenues, 2), "%")

employees_number = input("Введите количество сотрудников фирмы\n >>>")

if not employees_number.isdigit():
    employees_number = input("Введите количество сотрудников фирмы\n >>>")


print("Прибыль фирмы в расчёте на одного сотрудника равна", round(result / int(employees_number), 2))
