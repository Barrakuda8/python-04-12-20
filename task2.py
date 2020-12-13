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
    print(f"{name.title()} {surname.title()} {birth_year}-го года рождения, "
          f"живёт в {living_city.title()}. Email: {email}. Номер телефона: {phone}")


def pos_int_input(text: str) -> int:
    """ Function to make user input a positive integer
    :param text: text of input field
    :return: a positive integer
    """
    while True:
        user_num = input(text)
        if user_num.isdigit():
            return int(user_num)


user_data_output(name=input("Ваше имя: "), surname=input("Ваша фамилия: "),
                 birth_year=pos_int_input("Год рождения: "), living_city=input("В каком городе вы живёте: "),
                 email=input("Ваш электронный адрес: "), phone=input("Ваш номер телефона: "))
