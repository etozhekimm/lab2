def summary(mas, inx):
    if int(mas[inx]) > 0:
        return summary(mas, inx + 1) + int(mas[inx])
    else:
        return 0


ms = input()
print(summary(ms.split(), 0))
