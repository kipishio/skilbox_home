# Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: С днём рождения, {name}! С {age}-летием тебя!
#
# Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
#
# Возраст людей через пробел: 20 30 18
#
# С днём рождения, Иван Иванов! С 20-летием тебя! С днём рождения, Петя Петров! С 30-летием тебя! С днём рождения, Лена Ленова! С 18-летием тебя!
#
# Именинники: Иван Иванов 20, Петя Петров 30, Лена Ленова 18

template = input(' Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')

while True:
    if '{name}' in template and '{age}' in template:
        break
    print('В шаблоне должны быть указаны все конструкци: ')
    template = input(' Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')

people_name_list = input('Список людей через запятую: ').split(', ')

age_list = input('Возраст людей через пробел: ').split()

for i in range(len(people_name_list)):
    print(template.format(name=people_name_list[i], age=age_list[i]))

birthday_list = [" ".join([people_name_list[i], age_list[i]]) for i in range(len(people_name_list))]
birthday = ', '.join(birthday_list)

print(birthday)


