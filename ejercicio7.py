"""
    El constructor de la clase recibe dos parámetros: titular (que es un objeto de la clase Persona) y cantidad (opcional, con valor 0.0 si no se especifica).
    Los atributos de la clase son privados, por lo que se utilizan los métodos getters para acceder a ellos.
    El método mostrar() imprime en pantalla los datos de la cuenta.
    El método ingresar() recibe una cantidad y la suma a la cantidad actual de la cuenta, siempre y cuando la cantidad sea mayor que 0. Si no lo es, no se hace nada.
    El método retirar() recibe una cantidad y la resta a la cantidad actual de la cuenta, siempre y cuando la cantidad sea mayor que 0. Si no lo es, no se hace nada. La cuenta puede quedar en números rojos.
"""
from ejercicio6 import Persona

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular:", self.__titular.get_nombre())
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


# Importamos un objeto persona del ejercicio 6 con los datos vacíos
p = Persona()

# Seteamos los atributos utilizando los setters
p.set_nombre("Juan")
p.set_edad(25)
p.set_dni("12345678")


# Creamos una cuenta con el titular Juan y 1000 de saldo inicial
c = Cuenta(p, 1000)

# Mostramos los datos de la cuenta
c.mostrar()

# Ingresamos 500 a la cuenta
c.ingresar(500)

# Retiramos 200 de la cuenta
c.retirar(200)

# Mostramos los datos actualizados de la cuenta
c.mostrar()
