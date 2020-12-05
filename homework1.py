name = "Том"
surname = "Реддл"
age = 16

print("Меня зовут",name,surname,"мне",age,"лет")

user_name = input("А тебя как зовут?\n >>>")
user_age = input("Сколько тебе лет, " + user_name + "\n >>>")
user_answer_snakes = input("Ты любишь змей?\n >>>")

if user_name == "Гарри":
    print("Это всё Хагрид")
else:
    print("Привет,",user_name,user_age,"лет отроду. Твой Ответ:",user_answer_snakes)

