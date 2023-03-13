import math

"""
La función calcular_mcm() recibe dos argumentos num1 y num2 que corresponden a los números para los que se quiere calcular el mcm. 
La función utiliza la fórmula: mcm(a, b) = |a*b| / gcd(a, b) para calcular el mcm y lo retorna.
"""

def calcular_mcm(num1, num2):
    return abs(num1*num2)//math.gcd(num1, num2)

num1 = 12
num2 = 18

print("El mcm de", num1, "y", num2, "es:", calcular_mcm(num1, num2))


def mcm(a, b):
    """
    Calcula el mínimo común múltiplo (mcm) de dos números utilizando el máximo común divisor (MCD).
        Primero, definimos una función mcd que utiliza el algoritmo de Euclides para calcular el máximo común divisor de dos números.
    Luego, la función mcm utiliza la fórmula mcm(a, b) = (a * b) / MCD(a, b) para calcular el mínimo común múltiplo de los dos números.
    La función mcm llama a la función mcd para obtener el máximo común divisor de los dos números, y luego divide el producto de los dos números por este valor para obtener el mínimo común múltiplo.
    """
    def mcd(a, b):
        """
        Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
        """
        while b != 0:
            a, b = b, a % b
        return a
    
    return (a * b) // mcd(a, b)


a = 4
b = 6
print("El mcm de", a, "y", b, "es", mcm(a, b))
