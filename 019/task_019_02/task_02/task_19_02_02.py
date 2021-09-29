def count(product):
    summs = 0
    price = None
    price_name = ''
    for name in product:
        summs += product[name]
        if price is not None:
            if price > product[name]:
                price = product[name]
                price_name = name
        else:
            price = product[name]
    print('Результат работы программы:\n')
    print('Общий доход за год составил {0} рублей\n'.format(summs))
    print('Самый маленький доход у {0}. Он составляет {1} рублей\n'.format(price_name, product[price_name]))
    product.pop(price_name)
    print('Итоговый словарь: {0}'.format(incomes))



incomes = {
'apple': 5600.20,
'orange': 3500.45,
'banana': 5000.00,
'bergamot': 3700.56,
'durian': 5987.23,
'grapefruit': 300.40,
'peach': 10000.50,
'pear': 1020.00,
'persimmon': 310.00,
}

count(incomes)

