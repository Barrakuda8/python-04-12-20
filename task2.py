def user_data_output(name, surname, birth_year, living_city, email, phone):
    print(f"{name.title()} {surname.title()} родился(ась) в {birth_year} году, живёт в {living_city.title()}. Email: {email}. Номер телефона: {phone}")


def pos_int_input(text):
    while True:
        user_num = input(text)
        if user_num.isdigit():
            user_num = int(user_num)
            break
    return user_num


user_name = input("Ваше имя: ")
user_surname = input("Ваша фамилия: ")
user_year = int_input("Год рождения: ")
user_city = input("В каком городе вы живёте: ")
user_email = input("Ваш электронный адрес: ")
user_phone = input("Ваш номер телефона: ")


user_data_output(name=user_name, surname=user_surname, birth_year=user_year, living_city=user_city, email=user_email, phone=user_phone)


