class Triangle:
    def __init__(self, side, side2, side3):
        self.side = side
        self.side2 = side2
        self.side3 = side3
    def parameter (self):
        PA = self.side + self.side2 + self.side3
        return PA
    def area (self):
        s = self.parameter()/2
        area = (s*(s-self.side)*(s-self.side2)*(s-self.side3))**(1/2)
        return area