#!/usr/bin/env python3

# example class 3


def duplicar(lista):
    y=[]
    for elemento in lista:
        y.append(2*elemento)
    return y

x=[1,2,3]

print(x)
print(duplicar(x))
