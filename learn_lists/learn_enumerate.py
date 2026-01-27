# В Python функция enumerate() предоставляет удобный способ итерации по элементам списка с
# одновременным доступом к их индексам. Это особенно полезно, когда необходимо
# обрабатывать и индекс, и значение элемента списка в рамках цикла.
#
# Функция enumerate() оборачивает список в специальный объект и возвращает итератор,
# который производит кортежи (пары значений), состоящие из индекса и значения элемента

my_list1 = ["apple", "banana", "cherry"]
for index, element in enumerate(my_list1):
    print(f'Index: {index}, Element: {element}')

my_list2 = ["apple", "banana", "cherry"]
for index, element in enumerate(my_list2):
    if index % 2 == 0:
        print(f'Element {element} at even index {index}')