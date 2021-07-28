'''
Пример:
Введите строку: привет
Введите дополнительный символ: !
Список удвоенных символов: ['пп', 'рр', 'ии', 'вв', 'ее', 'тт']
Склейка с дополнительным символом: ['пп!', 'рр!', 'ии!', 'вв!', 'ее!', 'тт!']
'''

str_in = input("Введите строку: ")
str_symbol = input("Введите дополнительный символ: ")
doubled_symbol = [i*2 for i in str_in]
print("Список удвоенных символов: ", doubled_symbol)
list_additional_symbol = [i + str_symbol for i in doubled_symbol]
print("Склейка с дополнительным символом: ", list_additional_symbol)