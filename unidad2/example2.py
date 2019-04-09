#!/usr/bin/env python3

# example class 3

class MiLista:

    def __init__(self,contenido):
        self.contenido = contenido

    def __len__(self):
        return len(self.contenido)

    def multiplicar(self, mult):
        y=[]
        for elemento in self.contenido:
            y.append(mult*elemento)
        return y

    def duplicar(self):
        return self.multiplicar(2)

    def sumar(self):
        y=0
        for elemento in self.contenido:
            y = y + elemento
        return y

x=MiLista([1,2,3])

print(x.duplicar())
print(x.sumar())
print(len(x))
