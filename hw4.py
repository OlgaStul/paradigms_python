# Задача. Написать скрипт для расчета корреляции Пирсона междлу двумя случайными величинами (массивами).
#         Рекомендуется использовать функциональную парадигму.

from random import randint

list_x, list_y = [], []
for i in range(20):
    list_x.append(randint(0, 1000))
    list_y.append(randint(0, 1000))


def correlation(list_x, list_y):
    m_x = sum(map(lambda x: x, list_x)) / len(list_x)
    m_y = sum(map(lambda y: y, list_y)) / len(list_y)
    list_1 = list(map(lambda x: x - m_x, list_x))
    list_2 = list(map(lambda y: y - m_y, list_y))
    list_3 = list(map(lambda x, y: x*y, list_1, list_2))
    return sum(map(lambda x: x, list_3)) / (sum(map(lambda x: x*x, list_1)) * sum(map(lambda y: y*y, list_2)))**0.5


print(correlation(list_x, list_y))

# Использовалась процедурная, структурная и функциональная парадигмы
