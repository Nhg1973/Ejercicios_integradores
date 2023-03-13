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
