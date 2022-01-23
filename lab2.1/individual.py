priceSweets = int(input("Конфеты, цена за кг.:"))
priceCookie = int(input("Печенье, цена за кг.:"))
priceApple = int(input("Яблоки, цена за кг.:"))

amountSweets = int(input("Сколько кг. конфет купили?:"))
amountCookie = int(input("Сколько кг. печенья купили?:"))
amountApple = int(input("Сколько кг. яблок купили?:"))

allSum = (amountSweets * priceSweets) + (amountCookie * priceCookie) + (amountApple * priceApple)
print("Заплатите ", allSum, " рублей.")
