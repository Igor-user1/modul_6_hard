class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=False):
        if len(__sides) == self.sides_count:
            self.__sides = __sides
        else:
            if isinstance(self, Circle):
                __sides = [1]
                self.__sides = __sides
            elif isinstance(self, Triangle):
                __sides = [1, 1, 1]
                self.__sides = __sides
            elif isinstance(self, Cube):
                if len(__sides) != 1:
                    __sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                    self.__sides = __sides
                else:
                    list_1 = list(__sides)
                    while len(list_1) <= 12:
                        list_1.append(__sides[0])
                    self.__sides = list_1
        self.__color = __color
        self.filled = filled

    def __repr__(self):
        return self.__color, self.__sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r in range(256):
                if g in range(256):
                    if b in range(256):
                        self.__color = (r, g, b)
        else:
            return print('данные числа некорректные')

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            return self.__color

    def __is_valid_sides(self, *__sides):
        for i in self.__sides:
            if isinstance(i, int):
                if i > 0:
                    if len(self.__sides) == self.sides_count:
                        return True

    def get_sides(self):
        return self.__sides

    def __len__(self, *__sides):
        p = 0
        if self.__is_valid_sides(*__sides):
            for j in self.__sides:
                p += j
            return int(p)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def _radius_(self):
        import math
        __radius = self.get_sides()[0]/(2*math.pi)
        return __radius

    def get_square(self):
        import math
        square = math.pi*self._radius_()**2
        return square


class Triangle(Figure):
    sides_count = 3

    def get_square(self, *args):
        import math
        triangle_sides = self.get_sides()
        half_perimetr = int(self.__len__(*args))/2
        triangle_square = math.sqrt(half_perimetr*(half_perimetr - triangle_sides[0]) *
                                    (half_perimetr - triangle_sides[1]) *
                                    (half_perimetr - triangle_sides[2]))
        return triangle_square


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        v = self.get_sides()[0]**3
        return v


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
