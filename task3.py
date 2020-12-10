
seasons = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

while True:
    month = input("Введите месяц в виде целого числа: ")
    if month.isdigit():
        month = int(month)
        if not 1 <= month <= 12:
            continue
        break

for season, months in seasons.items():
    if month in months:
        print(f"Время года: {season}")
        break

