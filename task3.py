class NotANumber(Exception):

    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def number_verification(cls, item):
        try:
            return int(item)
        except ValueError:
            try:
                return float(item)
            except ValueError:
                raise NotANumber("Необходимо было ввести число")


user_list = []
while True:
    try:
        user_item = input("Для окончания ввода чисел нажмите 'Enter'\nВведите число: ")
        if user_item != "":
            user_list.append(NotANumber.number_verification(user_item))
        else:
            break
    except NotANumber as NAN:
        print(NAN.txt)

print(user_list)