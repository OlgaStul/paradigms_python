# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))

def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        minimum = i
        
        for j in range(i + 1, len(numbers)):
            # Выбор наименьшего значения
            if numbers[j] < numbers[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        numbers[minimum], numbers[i] = numbers[i], numbers[minimum]
            
    return numbers

def sort_list_declarative(numbers):
    return sorted(numbers)

print(sort_list_imperative(numbers))
print(sort_list_declarative(numbers))