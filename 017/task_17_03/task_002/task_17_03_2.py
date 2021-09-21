original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

print("Старый список:", original_prices)

new_list = [(i if i > 0 else 0) for i in original_prices]
print("Новый список:", new_list)