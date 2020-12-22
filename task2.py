import os

file_path = os.path.join(os.path.dirname(__file__), "files", "task2.txt")

with open(file_path, "r", encoding="UTF-8") as file:
    result = []
    for line in file:
        result.append((len(line.split())))

print(f"Количество строк в файле: {len(result)}. Количество слов в каждой строчке соответственно: {result}")
