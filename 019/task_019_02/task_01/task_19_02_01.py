def market(wan_dict, tow_dict):
    wan_dict.update(tow_dict)
    wan_dict.update(small_storage)
    name = input("Введите название товара: ")
    # print(wan_dict)
    if wan_dict.get(name) is None:
        print("Товара {0} не существует!".format(name))
    else:
        print(name, '-', wan_dict[name])


small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

market(big_storage, small_storage)
