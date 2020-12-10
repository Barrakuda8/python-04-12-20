
while True:
    list_length = input("Введите длину массива: ")
    if list_length.isdigit():
        list_length = int(list_length)
        break

user_list = []

for i in range(list_length):
    user_list.append(input("Добавьте элемент в список: "))
    i += 1

new_list = []

for i in range(0, list_length, 2):
    if list_length % 2 == 1 and i == list_length - 1:
        new_list.append(user_list[i])
    else:
        new_list.append(user_list[i + 1])
        new_list.append(user_list[i])
    i += 2

print(new_list)

