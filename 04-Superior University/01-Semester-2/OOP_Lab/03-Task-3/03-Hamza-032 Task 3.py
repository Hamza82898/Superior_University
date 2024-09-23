class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def __str__(self):
        return f"rectangle:{self.width} * {self.height}"
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)

while True:
    width=int(input("Enter a Width:"))
    height=int(input("Enter a Height:"))
    rectangle=rectangle(width,height)
    break

print(rectangle)

print(f"Area of Rectangle is {rectangle.area()}")
print(f"Perimeter of Rectangle is {rectangle.perimeter()}")