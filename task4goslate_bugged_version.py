import os
import goslate

translator = goslate.Goslate()

file_path = os.path.join(os.path.dirname(__file__), "files", "task4.txt")
file_path2 = os.path.join(os.path.dirname(__file__), "files", "task4_2.txt")

with open(file_path, "r", encoding="UTF-8") as file:
    with open(file_path2, "w", encoding="UTF-8") as file2:
        for line in file:
            result = translator.translate(line, 'ru')
            file2.write(result + "\n")


