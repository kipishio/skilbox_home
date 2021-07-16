number_team = int(input('Кол-во участников: '))
number_human = int(input('Кол-во человек в команде: '))
list_peoples = []
numb = 1

for i_team in range(number_team):
    list_peoples.append(list(range(numb, numb + number_human)))
    numb += number_human
    people = []
print(list_peoples)
