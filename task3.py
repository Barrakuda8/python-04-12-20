def two_out_of_three(num1, num2, num3):
    num_list = [num1, num2, num3]
    num_list.remove(min(num_list))
    result = sum(num_list)
    return result


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


user_sum = two_out_of_three(float_input("Введите 1 число: "), float_input("Введите 2 число: "), float_input("Введите 3 число: "))
print(better_float_output(user_sum, 2))

