import os
import re

file_path = os.path.join(os.path.dirname(__file__), "files", "task6.txt")

timetable = {}

with open(file_path, "r", encoding="UTF-8") as file:
    for line in file:
        timetable[line.split(':')[0]] = sum(list(map(int, re.findall("(\d+)", line))))

print(timetable)
