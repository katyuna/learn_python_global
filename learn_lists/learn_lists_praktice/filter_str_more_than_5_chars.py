# Фильтрация строк
# Дан список строк. Создай новый список, содержащий только строки длиной больше 5 символов.

first_list = ["qwe", "tryrys", "er", "dgshkbksbkdsbkb", "nhjkj"]

str_list = [x for x in first_list if len(x)>5]
print(str_list)