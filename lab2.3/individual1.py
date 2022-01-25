word = str(input("Введите строку:"))
part1 = str(input("Введите первый символ:"))
part2 = str(input("Введите второй символ:"))
print("\n", "Координаты вхождений первого символа:", end='')
for i in range(len(word) - 1):
    if word[i] == part1:
        print(' ', i, end='')
print("\n", "Координаты вхождений второго символа:", end='')
for i in range(len(word) - 1):
    if word[i] == part2:
        print(' ', i, end='')
