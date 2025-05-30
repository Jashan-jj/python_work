class shapeCalculator:
    def area(self, a = None, b=None):
        if a is not None and b is None:
            return a * a * 3.141
        elif a is not None and b is not None:
            return a*b
        else:
            print("invalid input")

c = shapeCalculator()
print(c.area(2))
print(c.area(5, 5))
