def divide(dividend: float, divisor: float) -> float or int:
    """ Function to divide one number by another
    :param dividend: number to divide
    :param divisor: number to divide by
    :return: result
    """
    try:
        return round(dividend / divisor, 4)
    except ZeroDivisionError:
        print("Нельзя делить на 0")
        exit()


def better_float_output(number: float, decimal=2) -> float or int:
    """ Function to make decimal number look better
    :param number: decimal number to be beautiful
    :param decimal: number of decimal places
    :return: Belle
    """
    if number % 1 == 0:
        return round(number)
    else:
        return round(number, decimal)


def float_input(text: str) -> float:
    """ Function to make user input a number
    :param text: text of input field
    :return: a number (float type)
    """
    while True:
        user_num = input(text)
        try:
            return float(user_num)
        except ValueError:
            continue


print("Частное:", better_float_output(divide(float_input("Введите делимое: "),
                                             float_input("Введите делитель: ")), 2))
