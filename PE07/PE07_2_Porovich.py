class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
   
    # Redefining p1.__str__() --> our point coordinate system
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # redefining __add__ function to overload an existing operator
    def __add__(self, rhs):
        return self.x + rhs.x, self.y + rhs.y
    
    # redefining __sub__ function to overload '-' operator
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y
    
    # redefining __gt__ function to overload '>' operator
    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        else:
            return False


p1 = Point(13, 15)
p2 = Point(-1, 8)

print(p1)
print(p2)
print(p1 + p2) # p1+p2 ==> p1.__add__(p2), p1 <= self, p2 <= rhs
print(p1 - p2) # p1-p2 ==> p1.__sub__(p2), p1 <= self, p2 <= other
print(p1 > p2) # p1>p2 ==> p1.__gt__(p2), p1 <= self, p2 <= other
