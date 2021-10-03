def country_info(count_):
    for i in range(count_):
        country = input('{0} страна: '.format(i + 1))
        print()
        country_split = country.split()
        geography_dict[country_split[0]] = set(country_split[1:])
        # print(geography_dict)
    print()

    for i in range(count_):
        info_town = True
        town = input('{0} город: '.format(i+1))
        print()
        for country_i in geography_dict:
            if town in geography_dict[country_i]:
                print('Город {0} расположен в стране {1}.\n\n'.format(town, country_i))
                info_town = False
                break
        if info_town:
            print('По городу {0} данных нет.'.format(town))


geography_dict = dict()

count = int(input('Кол-во стран: '))
print()
country_info(count)
