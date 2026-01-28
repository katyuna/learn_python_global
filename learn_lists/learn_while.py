numbers = [1, 2, 3, 4, 5, -1, 6]
i = 0
while i < len(numbers) and numbers[i] != -1:
    print(numbers[i])
    i += 1

tasks = [1, 2, 3, 4, 5, -1, 6]
while len(tasks) > 0:
    task = tasks.pop()
    print(task)