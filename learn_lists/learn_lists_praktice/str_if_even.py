# Создай список чисел от 1 до 30, где:
# четные числа заменены на строку "even"
# нечетные остаются числами

my_list = list(range(1,31))
print(my_list)
result = ["even" if x % 2 == 0 else x for x in range(1, 31)]
print(result)
