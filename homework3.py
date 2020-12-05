number = input("Введите целое положительное число: ")

while not number.isdigit():
    number = input("Введите целое положительное число: ")

term1 = int(number)
term2 = int(number + number)
term3 = int(number + number + number)

print(term1 + term2 + term3)



