class Family:
    surname = 'Петровы'
    money = 1000500
    having_a_home = False


    def info_fam(self):
        print('Фамилия: {}\nКол-во денег: {}\nВладение домом: {}'.format(self.surname, self.money, self.having_a_home))

    def earn_money(self, earned):
        self.money += earned

    def buy_house(self, house_value):
        if house_value > self.money:
            print("Денег не хватает попробуйте заработать")
        else:
            self.money -= house_value
            self.having_a_home = True



fam_1 = Family()
fam_1.info_fam()
fam_1.buy_house(1*10**6)

print()
fam_1.earn_money(600)
fam_1.buy_house(1*10**6)
fam_1.info_fam()
