class Point:
    __count = 0

    def __init__(self, coordinate_x=0, coordinate_y=0):
        self.set_coordinate(coordinate_x, coordinate_y)
        Point.__count += 1
        self.__index = Point.__count

    def __str__(self):
        return 'Координаты точки {} на плоскости X = {}, Y = {}'.format(self.__index, self.__coordinate_x, self.__coordinate_y)

    def get_count(self):
        return Point.__count

    def set_coordinate(self, coord_x, coord_y):
        self.__coordinate_x = coord_x
        self.__coordinate_y = coord_y

    def get_coordinate(self):
        pass

    def get_coordinate(self):
        return (self.__coordinate_x, self.__coordinate_y)



point_1 = Point(12, 8)
point_2 = Point(78, 15)
point_3 = Point(65,3)

print(point_1)
print(point_2)
print(point_3)
print(point_1.get_coordinate())
print(point_2.get_coordinate())
print(point_3.get_coordinate())
print('Всего задано {} точек'.format(point_1.get_count()))