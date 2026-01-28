# Дана строка. Создай список, содержащий только гласные буквы из этой строки (в любом регистре).

my_str = 'javgggeeeeguubbbbqeunndsjjbgg'
my_vowels = 'aeu'
my_vowels_list = [x for x in my_str if x in my_vowels]
print(my_vowels_list)
