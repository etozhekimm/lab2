def book(author, **books):
    print(f"Author: {author}")
    for books, name in books.items():
        print(f"{name}")


if __name__ == '__main__':
    book(
        "Э. М. Ремарк",
        book1="На западном фронте без перемен",
        book2="Триумфальная арка",
        book3="Три товарища"
    )
    book(
        "М. Ю. Лермонтов",
        book1="Герой нашего времени"
    )