# TODO приступим

# my_list = [1, 2, 3, 4, 5]
# iterarot = iter(my_list)
#
# def iter_list(my_iter):
#     while True:
#         try:
#             print(next(my_iter))
#         except StopIteration:
#             # print('Конец')
#             break
#
#
#
# iter_list(iterarot)

class my_kl:

    def __init__(self):
        self.cur_val = 0
        self.next_val = 1

    def next(self):
        self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
        print(self.cur_val)


rty = my_kl()

rty.next()
rty.next()
rty.next()
rty.next()
rty.next()
rty.next()
rty.next()
rty.next()
rty.next()