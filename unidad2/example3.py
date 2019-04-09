#!/usr/bin/env python3

# example class 3
from math import pi


class forma:

    def ratio(self):
        return self.area()/self.perimetro()

class circulo(forma):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio * self.radio

    def perimetro(self):
        return 2 * pi * self.radio

class cuadrado(forma):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio

    def perimetro(self):
        return 2 * self.radio

a2 = circulo(2)
c4 = cuadrado(4)
print(a2.area(),a2.perimetro(),a2.ratio())
print(c4.area(),c4.perimetro(),c4.ratio())
# print(c2.area())
# print(x.sumar())
