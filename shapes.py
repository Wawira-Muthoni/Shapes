# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# # It has a method to calculate circumference (c) using the formula C=2π

import math


class Circle:
    def __init__(self,r):
        self.r = r
    def area(self): 
        A = math.pi*(self.r**2)
        return A
    def circumference(self):
        C = (2*math.pi* (self.r))
        return C




# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4aC
class Square:
    def __init__(self,A):
        self.A = A
    def area (self):
            A = self.A*self.A
            return A

    def Perimeter(self):
        P =2*self.A+2*self.A   
        return P     
      

# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

    class Rectangle:
        def __init__ (self,l,w):
            self.l = l
            self.w = w
        def area(self):
          a = self.l*self.w
          return a
        def perimeter(self):
          p = 2*(self.l+self.w) 
          return p

# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
    class Sphere:
        def __init__(self,r):
            A = 4* math.pi*(self.r**r)
            return A
        def volume(self):
            v = 4/3*math.pi*self.r**3
            return v    






