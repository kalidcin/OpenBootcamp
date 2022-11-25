class Vehiculo:
    _color = "Rojo"
    _ruedas = 4
    _puertas = 5

class Coche(Vehiculo):
    _velocidad = 5
    _cilindrada = 4

c = Coche()
print("El coche es color: ",c._color)
print("Tiene {} ruedas".format(c._ruedas))