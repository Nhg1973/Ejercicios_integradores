
"""
La función calcular_mcd() recibe dos argumentos num1 y num2 que corresponden a los números para los que se quiere calcular el MCD. 
La función utiliza math.gcd() para calcular el MCD y lo retorna.
"""
import math

def calcular_mcd(num1, num2):
    return math.gcd(num1, num2)

num1 = 12
num2 = 18

print("El MCD de", num1, "y", num2, "es:", calcular_mcd(num1, num2))



def mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
    
        El algoritmo de Euclides se basa en la idea de que el MCD de dos números a y b es el mismo que el MCD de b y el resto de la división de a entre b (a % b).
    En cada iteración del bucle, se intercambian los valores de a y b, y se actualiza b como el resto de la división de a entre b.
    El bucle se repite hasta que b sea igual a cero, momento en el que el valor de a será el máximo común divisor de los dos números iniciales.
    """
    while b != 0:
        a, b = b, a % b
    return a

a = 24
b = 36
print("El MCD de", a, "y", b, "es", mcd(a, b))



