# ws_7_5.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.a = (width, height)

    def calculate_area(self):
        return self.width * self.height
        # return self.a[0] * self.a[1]
    
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
        # return self.a[0] * 2 + self.a[1] * 2
    
    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.calculate_area()}')
        print(f'Perimeter: {self.calculate_perimeter()}')

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'
        # return f'Shape: width={self.a[0]}, height={self.a[1]}'

shape1 = Shape(5, 3)
print(shape1)