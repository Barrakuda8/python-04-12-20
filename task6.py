from itertools import cycle, count
from sys import argv
from flinfunc import check

if len(argv) != 5:
    print("Надо было ввести числа начала и конца отсчёта, слово для повторения и количество символов в повторении")
    exit()

start = check(argv[1], "Число начала отсчёта должно быть целым положительным", cond="number > 0")
stop = check(argv[2], "Число конца отсчёта должно быть целым положительным", cond="number > 0")

if start > stop:
    print("Число начала отсчёта должно быть меньше числа конца отсчёта")
    exit()

for n in count(start):
    if n > stop:
        break
    else:
        print(n)

user_string = argv[3]
repeat = check(argv[4], "Количество символов в повторении должно быть целым положительным числом", cond="number > 0")

repeat_count = 0
for n in cycle(user_string):
    if repeat_count == repeat:
        break
    else:
        print(n)
    repeat_count += 1
