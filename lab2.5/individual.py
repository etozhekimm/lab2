import sys

if __name__ == '__main__':
    tpl = tuple(map(float, input().split()))
    if not tpl:
        print("Заданный кортеж пуст", file=sys.stderr)
        exit(1)

if tuple(sorted(tpl, reverse = True)) == tpl:
    print("Команды перечислены в соответствии с занятыми местами")
else:
    print("Команды перечислены не в соответствии с занятыми местами")
