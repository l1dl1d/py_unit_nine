class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def parameter(self):
        P = 2 * self.width + 2 * self.length
        return P
    def Area(self):
        area = self.width * self.length
        return area


