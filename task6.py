import re


def title_func(text: str) -> str:
    """ Function to make all words begin with a capital letter
    :param text: text to transform
    :return: transformed text
    """
    return text.title()


def latin_input(text: str) -> str:
    """ Function to make user input a text with only latin letters and spaces
    :param text: text of input field
    :return: text in latin alphabet (small letters)
    """
    while True:
        user_text = input(text)
        pattern = re.compile("[a-zA-Z ]+")
        if pattern.fullmatch(user_text):
            return user_text.lower()


print(title_func(latin_input("Введите слова через пробелы на латинице: ")))


