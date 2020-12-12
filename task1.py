def divide(dividend, divisor):
    try:
        result = round(dividend / divisor, 4)
        return result
    except ZeroDivisionError:
        print("Нельзя делить на 0")
        exit()


def better_float_output(number, decimal=2):
    if number % 1 == 0:
        return round(number)
    else:
        return round(number, decimal)


def float_input(text):
    while True:
        user_num = input(text)
        try:
            user_num = float(user_num)
            break
        except ValueError:
            continue
    return user_num


user_dividend = float_input("Введите делимое: ")
user_divisor = float_input("Введите делитель: ")


print("Частное:", better_float_output(divide(user_dividend, user_divisor), 2))

