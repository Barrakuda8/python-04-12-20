from flinfunc import input_list, better_float_output as bfo

user_list = list(map(bfo, input_list("Введите числа для списка через пробел: ", float)))

new_list = []

for el in user_list:
    if user_list.count(el) == 1:
        new_list.append(el)

print(new_list)
