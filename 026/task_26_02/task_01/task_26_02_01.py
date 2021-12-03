my_list = [1, 2, 3, 4, 5]
iterarot = iter(my_list)

def iter_list(my_iter):
    while True:
        try:
            print(next(my_iter))
        except StopIteration:
            break



iter_list(iterarot)
