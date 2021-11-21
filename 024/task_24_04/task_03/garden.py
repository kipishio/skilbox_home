class Potatoe:
    states = {0: 'Только посадили', 1: 'Пустила корни', 2: 'Зацвела', 3: 'Созрела'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def print_info(self):
        print('Картошка {} на стадии зрелости: {}'.format(self.index, Potatoe.states[self.state]))

    def grow_potato(self):
        if self.state < 4:
            self.state += 1
        print('Картошка {}, Стадия зрелости: {}'.format(self.index, Potatoe.states[self.state]))

    def is_ready(self):
        if self.state == 3:
            return True
        else:
            return False

class Bed_potatoes:
    def __init__(self, count):
        self.potatoes = [Potatoe(index) for index in range(1, count + 1)]

    def grow(self):
        print('\nКартошка проростает!')
        for i_potato in self.potatoes:
            i_potato.grow_potato()


    def check_potetos(self):
        if all([i_potato.is_ready() for i_potato in self.potatoes]):
            print('\nКартошка созрела можно собирать')
        else:
            print('\nКартошка еще не созрела')
