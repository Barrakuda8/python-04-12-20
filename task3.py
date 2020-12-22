import os

file_path = os.path.join(os.path.dirname(__file__), "files", "task3.txt")

with open(file_path, "r", encoding="UTF-8") as file:
    data = {}
    for line in file:
        el = line.split()
        data[el[0]] = int(el[1])

result = 0
for key, val in data.items():
    result += val
    if val <= 20000:
        print(key)

print(f"Средняя зп в России: {round(result / len(data))} руб")
