word1 = str(input("Введите первое слово:"))
word2 = str(input("Введите второе слово:"))
word3 = str(input("Введите третье слово:"))
repeat = ""

for i in range(len(word1)):
    for j in range(len(word2)):
        for k in range(len(word3)):
            if (word1[i] == word2[j]) and (word2[j] == word3[k]):
                repeat += word1[i]

sorted_repeat = sorted(repeat)
last = '0'
print("Общие буквы: ", end='')
if len(sorted_repeat) == 0:
    print("отсутствуют")
else:
    for i in range(len(sorted_repeat)):
        if sorted_repeat[i] != last:
            last = sorted_repeat[i]
            print(sorted_repeat[i], " ", end='')
