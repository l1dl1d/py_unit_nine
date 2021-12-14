import rectangle
import triangle
rect = rectangle.Rectangle(4, 5)
rect2 = rectangle.Rectangle(6, 2)
rect3 = rectangle.Rectangle(9, 4)
print("The first rectangle has a parameter of ", rect.parameter(), "and an area of", rect.Area())
print("The second rectangle has a parameter of ", rect2.parameter(), "and an area of", rect2.Area())
print("The third rectangle has a parameter of ", rect3.parameter(), "and an area of", rect3.Area())
tri = triangle.Triangle(6, 4, 3)
tri2 = triangle.Triangle(5, 4, 3)
tri3 = triangle.Triangle(3, 7, 5)
print("The first triangle has a parameter of ", tri.parameter(), "and an area of", tri.area())
print("The second triangle has a parameter of ", tri2.parameter(), "and an area of", tri2.area())
print("The third triangle has a parameter of ", tri3.parameter(), "and an area of", tri3.area())