first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if x != y)
second_result = (len(first[x]) == len(second[x]) for x in range(len((first, second)) + 1))

print(list(first_result))
print(list(second_result))
