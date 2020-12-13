def degree(number: float, deg: int) -> float:
    """ Function to raise a number to a negative power
    :param number: number to raise
    :param deg: dark side level
    :return: raised number (float type)
    """
    result = 1
    i = -1
    while i >= deg:
        result = result / number
        i -= 1
    return result


def pos_float_input(text: str) -> float:
    """ Function to make user input a positive number
    :param text: text of input field
    :return: a positive number (float type)
    """
    while True:
        user_num = input(text)
        try:
            user_num = float(user_num)
            if user_num > 0:
                return user_num
        except ValueError:
            continue


def neg_int_input(text: str) -> int:
    """ Function to make user input a negative integer
    :param text: text of input field
    :return: a negative integer
    """
    while True:
        user_num = input(text)
        try:
            user_num = int(user_num)
            if user_num < 0:
                return user_num
        except ValueError:
            continue


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


print(better_float_output(degree(pos_float_input("Введите число: "),
                                 neg_int_input("Введите отрицательную степень: ")), 6))
