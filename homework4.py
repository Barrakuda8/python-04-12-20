number = input("Введите целое положительное число: ")

while not number.isdigit():
    number = input("Введите целое положительное число: ")
else:
    number = int(number)

temp_number = number
remainder = int
answer = 0

while not temp_number // 10 == 0:
    remainder = temp_number % 10
    temp_number = temp_number // 10
    if remainder > answer:
        answer = remainder
else:
    if temp_number > answer:
        answer = temp_number

print("Самая большая цифра в числе", number, "это", answer)

