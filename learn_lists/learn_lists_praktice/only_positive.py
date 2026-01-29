# Создай список из 10 случайных целых чисел от -50 до 50,
# затем создай второй список, содержащий только положительные числа из первого.

my_list = list(range(-50, 50))
print(my_list)

positive_list = [x for x in my_list if x>=0]
print(positive_list)