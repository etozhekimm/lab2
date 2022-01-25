message = str(input("Задайте предложение:"))
letter = str(input("Задайте букву:"))
result = ""
last = 0
for i in range(len(message) - 1, -1, -1):
    result += message[i]
    if (message[i] == "и") and (not last):
        result += letter
        last = 1
print(result[::-1])
