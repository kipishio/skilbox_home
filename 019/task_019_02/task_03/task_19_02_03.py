def count(text):
    count_alpha = dict()
    for alp in text:
        if alp in count_alpha:
            count_alpha[alp] += 1
        else:
            count_alpha[alp] = 1
    for name in count_alpha.keys():
        print('{0}:{1} '.format(name, count_alpha[name]), end=' ')
    print("Максимальная частота: {0}".format(max(count_alpha)))
alpha = sorted(input('Введите текст: ').lower())

count(alpha)
# print(alpha)