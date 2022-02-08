#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def film(director, **films):
    print(f"Режиссёр: {director}")
    for films, name in films.items():
        print(f"{name}")


if __name__ == '__main__':
    film(
        "Квентин Тарантино",
        book1="Бешеные псы",
        book2="Криминальное чтиво",
        book3="Омерзительная восьмерка"
    )
    film(
        "Дэвид Финчер",
        book1="Бойцовский клуб"
    )