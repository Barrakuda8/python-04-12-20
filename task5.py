import keyboard


def nums_input(text):
    while True:
        user_nums = input(text)
        user_nums = list(user_nums.split(" "))
        if "*" in user_nums[-1]:
            user_nums.remove("*")
            try:
                user_nums = list(map(float, user_nums))
                user_nums.append("*")
                return user_nums
            except ValueError:
                continue
        else:
            try:
                return list(map(float, user_nums))
            except ValueError:
                continue


def better_float_output(number, decimal=2):
    if number % 1 == 0:
        return round(number)
    else:
        return round(number, decimal)


result = 0
while True:
    user_numbers = nums_input("Введите числа через пробел: ")
    if "*" in user_numbers:
        user_numbers.remove("*")
        user_numbers = list(map(better_float_output, user_numbers))
        result += sum(user_numbers)
        print(f"Сумма чисел равна {result}")
        exit()
    else:
        user_numbers = list(map(better_float_output, user_numbers))
        result += sum(user_numbers)
        print(f"Сумма чисел: {','.join(list(map(str, user_numbers)))} равна {result}\n"
              f"Для ввода дополнительных чисел нажмите 'Enter'\n"
              f"Для завершения программы введите '*'")
        keyboard.wait('Enter')

