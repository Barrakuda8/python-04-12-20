data = input("Введите время в секундах: ")

while not data.isdigit():
    data = input("Пожалуйста, введите целое положительное число: ")
else:
    data = int(data)

minutes_count = data // 60
seconds_count = data % 60
hours_count = minutes_count // 60
minutes_count = minutes_count % 60

time = f"{hours_count}:{minutes_count}:{seconds_count}"
print(time)