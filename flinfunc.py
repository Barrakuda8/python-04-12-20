def need_input(text, func=int, cond="True"):
    while True:
        number = input(text)
        try:
            number = func(number)
            if eval(cond):
                return number
        except ValueError:
            continue


def better_float_output(number, decimal=2):
    if number % 1 == 0:
        return round(number)
    else:
        return round(number, decimal)


def input_list(text, func=int):
    while True:
        user_list = input(text)
        user_list = user_list.split()
        try:
            return list(map(func, user_list))
        except ValueError:
            continue


def list_generator(text, func=int):
    user_list = []
    while True:
        el = input(text)
        if el == "":
            break
        try:
            user_list.append(func(el))
        except ValueError:
            continue
    return user_list


def check(number, text, func=int, cond="True"):
    try:
        number = func(number)
        if eval(cond):
            return number
    except ValueError:
        pass
    print(text)
    exit()


