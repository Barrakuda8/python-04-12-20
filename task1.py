import os

file_path = os.path.join(os.path.dirname(__file__), "files", "task1.txt")

with open(file_path, "w", encoding="UTF-8") as file:
    while True:
        data = input("Введите строку в файл. Для завершения введите пустую строку: ")
        if data:
            file.write(data + "\n")
        else:
            break
