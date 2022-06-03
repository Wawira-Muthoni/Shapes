# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)


class Rectangle:
    def __init__ (self,l,w):
        self.length = l
        self.width = w
     

    def rectangle_area(self):
        return self.length*self.width

    def rectangle_perimeter(self):
        return self.length+self.width     
        
         

