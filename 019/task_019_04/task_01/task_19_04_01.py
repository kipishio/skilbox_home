def kol_vo(text):
    nabor = set('".,;:!?".')
    count = 0
    for i in text:
        if i in nabor:
            count += 1
    return count


text = input('Введите строку: ')
print(kol_vo(text))


