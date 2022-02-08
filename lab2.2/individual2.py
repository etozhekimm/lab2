#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    year = int(input('Введите год: '))
    colours = ('зеленый', 'красный', 'желтый', 'белый', 'черный')
    colour = colours[year % 5]
    animals = ('обезьяна', 'курица', 'собака', 'свинья', 'мышь', 'корова', 'тигр', 'заяц', 'дракон', 'змея', 'лошадь',
               'овца')
    animal = animals[year % 12]
    print('Цвет: ', colour)
    print('Живтоное: ', animal)
