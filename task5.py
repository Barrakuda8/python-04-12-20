import os
import random

file_path = os.path.join(os.path.dirname(__file__), "files", "task5.txt")

with open(file_path, "w", encoding="UTF-8") as file:
    length = random.randint(1, 50)
    for i in range(length):
        file.write(str(random.randint(1, length)) + " ")

with open(file_path, "r", encoding="UTF-8") as file:
    result = sum(list(map(int, file.readline().split())))

print(result)
