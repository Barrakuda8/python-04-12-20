def two_out_of_three(num1: float, num2: float, num3: float) -> float:
    """ Function to throw the smallest of 3 numbers and do the sum of 2 left numbers
    :param num1: 1st number
    :param num2: 2nd number
    :param num3: 3rd number
    :return: the sum of two biggest numbers
    """
    num_list = [num1, num2, num3]
    num_list.remove(min(num_list))
    result = sum(num_list)
    return result


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
            user_num = float(user_num)
            break
        except ValueError:
            continue
    return user_num


user_sum = two_out_of_three(float_input("Введите первое число: "),
                            float_input("Введите второе число: "), float_input("Введите третье число: "))
print(better_float_output(user_sum, 2))

