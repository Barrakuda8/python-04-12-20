my_list = [7, 5, 3, 3, 2]

while True:
    user_number = input("Введите натуральное число: ")
    if user_number.isdigit():
        user_number = int(user_number)
        break

if user_number > my_list[0]:
    my_list.insert(0, user_number)
elif user_number <= my_list[-1]:
    my_list.append(user_number)
else:
    for i in range(len(my_list)):
        if my_list[i] >= user_number > my_list[i + 1]:
            my_list.insert(i + 1, user_number)
            break

print(my_list)
