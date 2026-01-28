# Фильтрация
# Напишите программу, которая создает список из 20 случайных чисел в диапазоне от 1 до 100
# с использованием List Comprehension.
# Затем с использованием List Comprehension создает новый список,
# содержащий только четные числа из исходного списка.
# Программа должна вывести оба списка.
import random

my_list = [random.randint(1,100) for i in range(20)]
print (my_list)
even_list = [x for x in my_list if x%2 ==0]
print (even_list)