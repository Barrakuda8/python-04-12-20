from flinfunc import better_float_output as bfo, list_generator as lg

user_list = list(map(bfo, lg("Введите число для списка. Для завершения нажмите 'Enter' без ввода числа\n>>> ", float)))

print(user_list)

new_list = []

for i in range(1, len(user_list)):
    if user_list[i] > user_list[i - 1]:
        new_list.append(user_list[i])

print(new_list)

