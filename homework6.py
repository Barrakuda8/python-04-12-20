first_day_result = float(input("Введите ваш результат за первый день (в километрах): "))
desired_result = float(input("Введите желаемый результат (в километрах): "))

# для красоты выводимого результата:
if desired_result % 1 == 0:
    desired_result = round(desired_result)

result = first_day_result
days_count = 1

while result < desired_result:
    result *= 1.1
    days_count += 1

print(f"На {days_count}-й день Вы достигните результата - не менее {desired_result} км, а точнее {round(result, 3)} км")