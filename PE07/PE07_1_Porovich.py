import math
class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.side_lengths = [5, 4] # set x and y side lengths
        
    # return number of sides    
    def getEdges(self): 
        if len(self.side_lengths) % 2 == 0:
            return 4
        else:
            return 3

    # return computed perimeter
    def computePerimeter(self): 
        perimeter = self.side_lengths[0] * 2 + self.side_lengths[1] * 2
        return perimeter
    
    # return the area of the rectangle
    def computeArea(self): 
        area = self.side_lengths[0] * self.side_lengths[1]
        return area
    
class Triangle(Shape):
    def __init__(self):
        self.side_lengths = [3, 6, 7] # 3 sides

    # return number of sides    
    def getEdges(self): 
        if len(self.side_lengths) % 2 == 0:
            return 4
        else:
            return 3
        
    # return computed perimeter
    def computePerimeter(self): 
        return sum(self.side_lengths)
    
    # return the area of the triangle given 3 sides
    def computeArea(self): 
        s = sum(self.side_lengths) / 2
        area = math.sqrt(s * (s - self.side_lengths[0]) * 
        (s - self.side_lengths[1]) * (s - self.side_lengths[2]))
        return area
    
# creating objects for rectangle and triangle
r = Rectangle()
t = Triangle()

# calling its methods to print the # of sides, perimeter and the area.
print(r.getEdges())
print(r.computePerimeter())
print(r.computeArea())

print(t.getEdges())
print(t.computePerimeter())
print(t.computeArea())