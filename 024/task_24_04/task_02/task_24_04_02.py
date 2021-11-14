class Point:
    count = 0

    def __init__(self, coordinate_x=0, coordinate_y=0):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        Point.count += 1
        self.index = Point.count

    def print_info(self):
        print('Координаты точки {} на плоскости X = {}, Y = {}'.format(self.index, self.coordinate_x, self.coordinate_y))

    def count_all_point(self):
        print('Всего создано {} точек'.format(self.count))



point_1 = Point(12, 8)
point_2 = Point(78, 15)
point_3 = Point(65,3)

point_1.count_all_point()
Point.count = 8
point_1.count_all_point()
point_2.print_info()
point_3.print_info()