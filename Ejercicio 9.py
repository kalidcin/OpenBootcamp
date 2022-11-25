class Alumno:
    _nombre = None
    _nota = 0

    def colocarNota(self, _nombre, _nota):
        self._nota = _nota
        self._nombre = _nombre

    def aprobo(self):
        if (self._nota < 7):
            print("El alumno {} ha reprobado con {}".format(self._nombre, self._nota))
        else:
            print("El alumno {} ha aprobado con {}".format(self._nombre, self._nota))

a = Alumno()
a.colocarNota("Kalid", 8)
a.aprobo()