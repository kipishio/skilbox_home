from beds import Bed_potatoes

bed_1 = Bed_potatoes(8)
bed_1.check_potetos()

for _ in range(3):
    bed_1.grow()
    bed_1.check_potetos()

