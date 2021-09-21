import colorsys
import random

original_prices = [random.randint(-10, 15) for _ in range(random.randint(5, 10))]

new_prices = original_prices[:]

new_prices = [(i if i > 0 else 0) for i in original_prices]


print(original_prices, end=' Сумма = ')
print(sum(original_prices))
print()

print(new_prices, end=' Сумма = ')
print(sum(new_prices))

print("Мы потеряли: ", sum(new_prices) - sum(original_prices))
