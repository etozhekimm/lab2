#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_student():
    # Запросить данные о человеке.
    name = input("Фамилия и имя? ")
    phone = input("Номер телефона? ")
    birth = input("Дата рождения? ")
    # Создать словарь.
    return {
        'name': name,
        'phone': phone,
        'birth': birth,
    }


def display_students(staff):
    if staff:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 13
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^13} |'.format(
                "No",
                "Фамилия и имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        print(line)
        # Вывести данные о всех людях.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>13} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('phone', ''),
                    student.get('birth', '')
                )
            )
        print(line)
    else:
        print("Список людей пуст")


def select_student(staff, phone):
    # Проверить сведения людей из списка.
    result = ""
    found = False
    for one in staff:
        if one.get('phone', '') == phone:
            result = one.get('name', '')
            found = True
    if not found:
        return "Нет человека с таким номером."
    else:
        return result


def date_key(birth):
    data = birth.split(".")
    return data[2], data[1], data[0]


def main():
    # Список людей.
    students = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о человеке
            student = get_student()
            # Добавить словарь в список
            students.append(student)
            # Отсортировать список в случае необходимости
            if len(students) > 1:
                students.sort(key=lambda item: date_key(item.get('birth', '')))
        elif command == 'list':
            # Отобразить всех людей
            display_students(students)
        elif command.startswith('phone '):
            # Разбить команду на части для выделения номера телефона.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый номер.
            phone = parts[1]
            # Отобразить выбранного человека
            print(select_student(students, phone))
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("phone <номер> - запросить человека по номеру;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
