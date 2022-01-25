import sys

if __name__ == '__main__':
    a = list(map(int, input().split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

sum = 0
amount = 0
for i in range(10):
    if ((a[i] % 7) == 0) and (a[i] < 0):
        amount += 1
        sum += a[i]
print("Количество отрицательных элементов кратных семи: ", amount)
print("Их сумма: ", sum)
