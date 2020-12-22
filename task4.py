import os

file_path = os.path.join(os.path.dirname(__file__), "files", "task4.txt")
file_path2 = os.path.join(os.path.dirname(__file__), "files", "task4_2.txt")

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open(file_path, "r", encoding="UTF-8") as file:
    with open(file_path2, "w", encoding="UTF-8") as file2:
        for line in file:
            result = line.split()
            result[0] = dictionary[result[0]]
            file2.write(" ".join(result) + "\n")
