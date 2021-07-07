word_search = []
count = [0, 0, 0]

for i in range(3):
    print('Введите', i + 1, 'слово: ', end='')
    word = input()
    word_search.append(word)

print(word_search)

text = ''

while text != 'end':
    text = input('Слово из текста: ')
    for index in range(3):
        if word_search[index] == text:
            count[index] += 1

print("\nПодсчет слов в тексте")

for index in range(3):
    print(word_search[index], ':', count[index])
print()