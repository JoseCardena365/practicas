class Persona:

    cabello = "negro"

    def __init__(self, edad, peso, nacionalidad, altura):   #__init__ es para crea un nuevo objeto.
        self.edad = edad
        self.peso = peso
        self.nacionalidad = nacionalidad
        self.altura = altura

def sentarse(self):
    print("La persona ejecuta la accion de sentarse")

def pararse(self):
    print("La persona ejecuta la accion de pararse")

    def descripcion(self):
        print(self.edad, self.peso, self.nacionalidad, self.altura)

jose = Persona(20, 80, "mexicana", 1.70)
angel = Persona(20, 80, "mexicana", 1.70)

#Herencia
class Alumno(Persona):
    def __init__(self, nombre, matricula, escuela):
        super().__init__(19, 87, "mexicana", 1.68)
        self.nombre = nombre
        self.matricula = matricula
        self.escuela = escuela

    def descripcion(self):
        print(self.nombre, " tiene: ", self.edad, ", pesa", self.peso, " estudia en: ", self.escuela, "y su matricula es: ", self.matricula)

# alumno = Alumno("kenny", "E123456", "ITM")
# alumno2 = Alumno("adnrea","F4567", "UADY")
#
# alumno.descripcion()
# alumno2.descripcion()
#
# jose.edad = 50
# jose.descripcion()
# angel.sentarse()
# jose.pararse()
#
# jose.descripcion()
# angel.descripcion()
# print(jose.cabello)
# print(angel.cabello)

from math import pi

class figura:
    def __init__(self, nombre_figura, color):
        self.nombre_figura = nombre_figura
        self.color = color

    def area(self):
        pass

class CirculoVerde(figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre, "verde")
        self.nombre = nombre
        self.radio = radio

    def area(self):
        return pi*self.radio**2

class TrianguloRojo(figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre, "rojo")
        self.base = base
        self.altura = altura

    def area (self):
        return(self.base*self.altura)/2

    def suma(self, area):
        print(area+10)

    def area2(self, base, altura):
        resultado = (base*altura)/2
        print(resultado)


circulo = CirculoVerde("circulit", 4)
triangulo = TrianguloRojo("triangulo equilatero", 3,4)
print(circulo.nombre)
print(triangulo.nombre_figura)
print(circulo.area())

#METODO CON return
print(triangulo.area())
#METODO CON PRINT
triangulo.area2(triangulo.base, triangulo.altura)
