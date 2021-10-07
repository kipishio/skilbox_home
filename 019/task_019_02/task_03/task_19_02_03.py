def count(text):
    count_alpha = dict()
    for alp in text:
        if alp in count_alpha:
            count_alpha[alp] += 1
        else:
            count_alpha[alp] = 1
    return count_alpha
    # for name in count_alpha.keys():
    #     print('{0}:{1} '.format(name, count_alpha[name]), end=' ')

    # print("Максимальная частота: {0}".format(max(count_alpha)))


alpha = input('Введите текст: ').lower()
hist = count(alpha)

for sym in sorted(hist.keys()):
    print(sym, ':', hist[sym])

print("Максимальное частота ", max(hist.values()))
