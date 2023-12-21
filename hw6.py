# from random import randint

# set_1 = set()
# for i in range(20):
#     set_1.add(randint(1, 100))


# def set_in_list(set_1):
#     list_1 = []
#     while len(set_1) != 0:
#         for i in set_1:
#             list_1.append(i)
#     return sorted(list_1)


# start и stop - индексы начала и конца списка, mid - индекс среднего элемента (деление целочисленное)
def binary_search(list_1, number, start, stop):
    if start > stop:
        return -1
    else:
        mid = (start + stop) // 2
        if number == list_1[mid]:
            return mid
        elif number < list_1[mid]:
            return binary_search(list_1, number, start, mid-1)
        else:
            return binary_search(list_1, number, mid+1, stop)


# list_1 = set_in_list(set_1)
# print(set_1)
# print(list_1)
list_5 = [5, 8, 9, 15, 34, 50, 57, 70, 86, 94, 95]
print(list_5)
number = int(input("Введите элемент, индекс которого вы хотите получить: "))
x = binary_search(list_5, number, 0, len(list_5))

if x == -1:
    print("Элемента {} нет в списке".format(number))
else:
    print("Элемент {} имеет индекс {}".format(number, x))
