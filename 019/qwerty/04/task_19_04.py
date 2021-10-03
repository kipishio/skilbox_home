goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
dict_goods = dict()
numb = 0

for i_goods in goods:
    # print(goods[i_goods])
    if store.get(goods[i_goods]) is not None:
        # print(store.get(goods[i_goods]))
        for i_store in store[goods[i_goods]]:
            # print(i_store)
            if dict_goods.get(i_goods) is not None:
                dict_goods[i_goods]['quantity'] = dict_goods[i_goods]['quantity'] + i_store['quantity']
                dict_goods[i_goods]['price'] = dict_goods[i_goods]['price'] + (i_store['price'] * i_store['quantity'])
            else:
                dict_goods[i_goods] = dict(quantity=0, price=0)
                dict_goods[i_goods]['quantity'] = dict_goods[i_goods]['quantity'] + i_store['quantity']
                dict_goods[i_goods]['price'] = dict_goods[i_goods]['price'] + (i_store['price'] * i_store['quantity'])

# print(dict_goods)
print('Результат работы программы.\n')
for name_goods in dict_goods:
    print('{0} - {1} шт, стоимость {2} руб.\n'.format(name_goods, dict_goods.get(name_goods).get('quantity'), dict_goods.get(name_goods).get('price')))

