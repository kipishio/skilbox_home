def my_print():
    print('привет')

def my_poka():
    print('пока')

my_print.jopa = 10
print(my_print.jopa)

my_print.poka = my_poka
my_print.poka()
my_print()

