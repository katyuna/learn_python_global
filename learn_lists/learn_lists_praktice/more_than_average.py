# Дан список чисел.
# Создай новый список, содержащий только числа больше среднего арифметического исходного списка.

def more_then_average(items) -> list:
    more_then_average_list = [item for item in items if item > sum(items)/len(items)]
    return more_then_average_list

print(more_then_average([1, 5, 3, 8, 2, 10]))


