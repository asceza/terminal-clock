#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep
import os
from datetime import datetime
from symbols import SYMBOLS


symbol_height = 7  # высота символа
symbols_width = 72  # ширина всего блока символов


def clear():
    os.system("clear")  # очищаем терминал



def translate(time_digit, blank):
    time_digit = str(time_digit)
    symbols = []
    for symbol in time_digit:
        symbols.append(SYMBOLS[symbol])
        # формируем список, где каждому символу соответсвует
        # пиксельная отрисовка из symbols.py


    for i in range(7):  # 7 - высота символа
        for j in range(blank):
            print(" ", end="")
              # печатаем пробелы в начале каждой строки для центровки по ширине


        # каждый пиксельный символ делится на строки (разделитель "\n")
        # end="  " явно указывает на пробел, без переноса на новую строку
        for symbol in symbols:
            print(symbol.splitlines()[i], end="  ")  # Добавляет в конце пробел
        print()  # явный перевод строки, для отрисовки новой строки в цикле


def show_clock():
    while True:
        # обрабатываем исключения CTRL + C (завершение скрипта)
        # в случае его появления - очищаем терминал в блоке except
        try:
            clear()

            # считаем количество пустых строк, необходимых для центровки надписи
            rows = round((os.get_terminal_size().lines - symbol_height) / 2)

            # печатаем пустые строки в цикле для центровки надписи по высоте
            i = 0
            while i < rows:
                print("")
                i += 1

            # считаем количество символов, необходимых для вставки перед надписью
            # чтобы ее отцентровать по ширине
            blank_width = round((os.get_terminal_size().columns - symbols_width) / 2)

            # определяем текущее время
            now_time = datetime.now()

            # создаем список из строк ч, м, с
            now_time_lst = [str(i) for i in [now_time.hour, now_time.minute, now_time.second]]
            now_time_lst_new = []

            # если длина строки равна 1, то добавляем 0 (например "7" -> "07")
            # сохраняем это в новый список
            for i in now_time_lst:
                if len(i) == 1:
                    now_time_lst_new.append("0" + i)
                else:
                    now_time_lst_new.append(i)

            # вызываем функцию, передаем ей аргументы
            # аргумент1 - строка с разделителем ":" на основе списка now_time_lst_new
            # аргумет2 - количество символов для центровки по ширине
            translate(":".join(now_time_lst_new), blank_width)
            sleep(0.1)
        except KeyboardInterrupt:
            clear()
            break


show_clock()
