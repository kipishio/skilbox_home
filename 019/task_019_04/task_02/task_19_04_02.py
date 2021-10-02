import random


def min_data(mnogestvo):
    minmum = 0
    for i in mnogestvo:
        minmum = i
        break
    for i in mnogestvo:
        if i < minmum:
            minmum = i
    return minmum


def redakt(l1, l2):
    nums_redakt_1 = set(l1)
    nums_redakt_2 = set(l2)
    print('1-е множество: {0}\n'.format(nums_redakt_1))
    print('2-е множество: {0}\n'.format(nums_redakt_2))

    min = min_data(nums_redakt_1)
    print('Минимальный элемент 1-го множества: {0}\n'.format(min))
    nums_redakt_1.discard(min)

    min = min_data(nums_redakt_2)
    print('Минимальный элемент 2-го множества: {0}\n'.format(min))
    nums_redakt_1.discard(min)

    numb = random.randint(1, 100)
    print('Случайное число для 1-го множества: {0}\n'.format(numb))
    nums_redakt_1.add(numb)

    numb = random.randint(1, 100)
    print('Случайное число для 2-го множества: {}\n'.format(numb))
    nums_redakt_1.add(numb)

    nums_obed = nums_redakt_1.union(nums_redakt_2)
    print('Объединение множеств: {0}\n'.format(nums_obed))

    nums_diff = nums_redakt_2.difference(nums_redakt_1)
    print('Элементы, входящие в nums_2, но не входящие в nums_1: {0}'.format(nums_diff))


nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

redakt(nums_1, nums_2)
