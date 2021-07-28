def up_percent(i_price, percent):
    return round(i_price + ((i_price/100)*percent), 2)

# round(i_price * (1 + percent / 100), 2)
# round(i_price + (i_price/100*percent))


# price_list = [float(input("Цена на товар: ")) for i in range(5)]
price_list = [1.09, 23.56, 57.84, 4.56, 6.78]
print(price_list)
fist_percent = int(input("Повышение на первый год: "))
second_percent = int(input("Повышение на второй год: "))


first_percent_list = [up_percent(i, fist_percent) for i in price_list]
print(first_percent_list)

second_percent_list = [up_percent(i, second_percent) for i in first_percent_list]
print(second_percent_list)
print("Сумма цен за каждый год: ", round(sum(price_list), 2), round(sum(first_percent_list),2), round(sum(second_percent_list), 2))
