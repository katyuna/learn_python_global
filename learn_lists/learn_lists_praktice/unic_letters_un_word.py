# text = "automation"
# Создай список из уникальных букв, сохранив порядок появления.
#уникальные как “встречаются ровно один раз”

text = "automation"
result = []

for letter in text:
    if text.count(letter) == 1:
        result.append(letter)

print(result)