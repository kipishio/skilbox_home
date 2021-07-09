def the_film_exists(film, name_films):
    for i_film in film:
        if i_film == name_films:
            return True
    return False



films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

my_films = []

while True:
    print("Ваш текущий топ фильмов: ", my_films)
    name_film = input('Название фильма: ')

    if not the_film_exists(films, name_film):
        print("Указанного фильма нет на сайте!!!")
        print("Укажите другой фильм.\n")
        continue

    print("Команды: добавить, вставить, удалить")
    print("Введите команду: ", end='')
    command = input()
    if command == "добавить":
        my_films.append(name_film)
    elif command == 'вставить':
        if the_film_exists(my_films, name_film):
            print("Фильм уже существует в вашем списке")
        else:
            index = (int(input("На какое место: ")))-1
            if index > len(my_films):
                print('Не правильно указанно место')
            elif index == len(my_films):
                my_films.append(name_film)
            elif index < len(my_films):
                my_films.insert(index, name_film)
    elif command == 'удалить':
        if the_film_exists(my_films, name_film):
            my_films.remove(name_film)
        else:
            print("Фильма нет в вашем избранном списке!!!\n")
    else:
        print("Команда не существует!!!\n")







