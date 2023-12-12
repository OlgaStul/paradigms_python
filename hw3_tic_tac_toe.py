''' Задача. Реализовать игру "Крестики-нолики". '''

field = list(range(1, 10))  # список ячеек поля
win_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8),
            (3, 6, 9), (1, 5, 9), (3, 5, 7)]  # список кортежей победных комбинаций

''' Показать поле '''


def show_field():
    print("-------------")
    for i in range(3):
        print("|", field[0 + i*3], "|", field[1 + i*3], "|", field[2 + i*3])
    print("-------------")


'''
Постановка х или о.
Пользователь делает ход - выбирает ячейку, в которую поставить предложенный символ.
Проверяем, если номер ячейки в пределах поля, то проверяем, если она свободна от X и O, то добавляем
символ в эту ячейку и прерываем цикл. Если нет, то оператором continue возвращаем к началу цикла.
'''


def input_x(symbol):
    while True:
        s = int(input("Куда хотите поставить {}? Введие номер ячейки: ".format(symbol)))
        if 1 <= s <= 9:
            if str(field[s-1]) in "XO":
                print("Эта ячейка занята. Попробуйте еще раз.")
                continue
            field[s-1] = symbol
            break
        else:
            print("Такой ячейки нет. Повторите ввод.")
            continue


'''
Проверка выигрышной комбинации.
Перебираем список кортежей по одному кортежу, затем элементы в кортеже по одному,
и от каждого элемента проверяем значение в списке ячеек. Если выполняется равенство, т.е.
при одной из выигрышных комбинаций оказываются одинаковыми значения на поле (все X или все O),
возвращаем это значение (X или O. В противном случае возвращаем False)
else стоит именно после цикла for. Если закончится весь перебор и не будет возвращено значение,
то вернуть False
'''


def check():
    for i in win_comb:
        if field[i[0] - 1] == field[i[1] - 1] == field[i[2] - 1]:
            return field[i[1] - 1]
    else:
        return False


'''
Напишем главную функцию main, в которой будут объединеты все наши объекты.
Пока в цикле истина - печатаем наше поле. Если четный ход, то ходят крестики, каждый нечетный ход будут
ходит нолики. Если на поле сделано более 3 ходов, проверяем выигрышные комбинации.
Если мы получили любое истинное значение отличное от False, то перерисовываем поле и выдаем победу.
Если число ходов еще не достигло 3, то увеличиваем counter на 1.
Когда количество попыток превысит 8, заполнится поле, последний раз перерисовываем поле, сообщаем - Ничья!
(функция chek() всегда возвращала False, продолжать игру смысла нет, выходим из цикла).

'''


def main():
    counter = 0         # нумерация хода
    while True:
        show_field()
        if counter %2 == 0:
            input_x('X')
        else:
            input_x('O')
        if counter > 3:
            winning = check()       # метод возвращает победивший символ или False
            if winning:             # если мы получили любое истинное значение отличное от False
                show_field()
                print(winning, "выиграл!")
                break
        counter += 1
        if counter > 8:
            show_field()
            print("Ничья!")
            break

print(main())
