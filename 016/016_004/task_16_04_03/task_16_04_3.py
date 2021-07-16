def fruit_price(fruit, price):
    list_fruit_price = [fruit, price]
    return list_fruit_price

print()
goods = [["яблоки", 50.0], ["апельсины", 190.0], ["груши", 100.0], ["нектарины", 200.0], ["бананы", 77.0]]
print('Текущий ассортимент: ', goods)
print()
fruit_name = input("Новый фрукт: ")
price = float(input('Цена: '))
print()
add_fruit = fruit_price(fruit_name, price)
goods.append(add_fruit)
print('Новый ассортимент: ', goods)

for i_goods in range(len(goods)):
    goods[i_goods][1] = goods[i_goods][1] + (goods[i_goods][1] / 100 * 8)
print()

print('Новый ассортимент с увел. ценой: ', goods)
