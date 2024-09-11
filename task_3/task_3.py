import doctest
class Rectangle:
    def __init__(self, width = 0, height=0):
        """
         >>> r = Rectangle(2, 3)
         >>> r.get_area()
         6
         >>> r.get_perimeter()
         10
         >>> r.set_dimensions(4,5)
         >>> print(r.width, r.height)
         4 5
        """
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        """
        >>> r = Rectangle()
        >>> r.set_dimensions(-1,0)
        Traceback (most recent call last):
        ...
        ValueError: Стороны не могут быть равны нулю или быть отрицательными
        """
        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            raise ValueError("Стороны не могут быть равны нулю или быть отрицательными")

    def get_area(self):
        '''
        >>> r = Rectangle(2,2)
        >>> r.get_area()
        4
        '''
        return self.width * self.height

    def get_perimeter(self):
        """
        >>> r = Rectangle(3,3)
        >>> r.get_perimeter()
        12
        """
        return self.width + self.width + self.height + self.height

if __name__ == '__main__':
    doctest.testmod(verbose=True)