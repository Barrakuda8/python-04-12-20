from functools import reduce

my_list = []
for number in range(100, 1001, 2):
    my_list.append(number)

print(my_list)
print(reduce(lambda a, b: a * b, my_list))