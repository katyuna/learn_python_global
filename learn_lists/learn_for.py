# Обход списка в прямом порядке
fruits1 = ["apple", "banana", "cherry"]
for fruit in fruits1:
    print(fruit)

# Обход списка в обратном порядке
fruits2 = ["apple", "banana", "cherry"]
for fruit in fruits2[::-1]:
    print(fruit)

# Цикл for с индексами
# Это позволяет работать не только с самими элементами, но и с их позициями

my_list1 = ['a', 'b', 'c', 'd']
for i in range(len(my_list1)):
    print(f'Index: {i}, Element: {my_list1[i]}')

# Модифицировать список во время итерации.
my_list2 = ['a', 'b', 'c', 'd']
for i in range(len(my_list2)):
    my_list2[i] = my_list2[i] * 2
    print(my_list2)

#Сравнение элементов
my_list = [3, 5, 2, 9, 4]
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        print(f'{my_list[i]} is greater than {my_list[i - 1]}')