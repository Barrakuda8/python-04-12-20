def user_data_output(name: str, surname: str, birth_year: int, living_city: str, email: str, phone: str):
    """ Function to output user data in one line
    :param name: user name
    :param surname: user surname
    :param birth_year: user year of birth
    :param living_city: city where user lives
    :param email: user email
    :param phone: user phone number
    :return: one line user information
    """
    print(f"{name.title()} {surname.title()} родился(ась) в {birth_year} году, "
          f"живёт в {living_city.title()}. Email: {email}. Номер телефона: {phone}")


def pos_int_input(text: str) -> int:
    """ Function to make user input a positive integer
    :param text: text of input field
    :return: a positive integer
    """
    while True:
        user_num = input(text)
        if user_num.isdigit():
            user_num = int(user_num)
            break
    return user_num


user_name = input("Ваше имя: ")
user_surname = input("Ваша фамилия: ")
user_year = pos_int_input("Год рождения: ")
user_city = input("В каком городе вы живёте: ")
user_email = input("Ваш электронный адрес: ")
user_phone = input("Ваш номер телефона: ")


user_data_output(name=user_name, surname=user_surname, birth_year=user_year,
                 living_city=user_city, email=user_email, phone=user_phone)


