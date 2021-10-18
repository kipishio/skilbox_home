def factorial(numb):
    if numb == 1:
        return 1
    return numb * factorial(numb - 1)


fact = int(input('Введите число факториал которого хотели бы узнать: '))
result_factorial = factorial(fact)
print(result_factorial)
