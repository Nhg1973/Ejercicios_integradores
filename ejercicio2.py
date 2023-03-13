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
