def degree(number, deg):
    result = number ** deg
    return result


def neg_float_input(text):
    while True:
        user_num = input(text)
        try:
            user_num = float(user_num)
            if user_num < 0:
                break
        except ValueError:
            continue
    return user_num


def pos_int_input(text):
    while True:
        user_num = input(text)
        if user_num.isdigit():
            user_num = int(user_num)
            break
    return user_num


def better_float_output(number, decimal=2):
    if number % 1 == 0:
        return round(number)
    else:
        return round(number, decimal)


print(better_float_output(degree(pos_int_input("Введите число: "), neg_float_input("Введите отрицательную степень: ")), 6))
