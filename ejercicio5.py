"""
a función utiliza un ciclo while infinito para pedir al usuario que ingrese un valor entero.
Se intenta convertir el valor ingresado en un número entero usando la función int().
Si el valor no es convertible en un número entero, se levanta una excepción ValueError, que se captura mediante un bloque try-except.
En caso de que se haya ingresado un valor válido, la función lo devuelve.
"""

def get_int():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("El valor ingresado no es un número entero. Intente nuevamente.")

"""
Solución Recursiva
    La función utiliza un bloque try-except para intentar convertir el valor ingresado en un número entero usando la función int().
    Si el valor no es convertible en un número entero, se levanta una excepción ValueError, que se captura mediante el bloque try-except.
    En caso de que se haya ingresado un valor válido, la función lo devuelve.
    Si se captura la excepción ValueError, la función imprime un mensaje de error y luego llama a sí misma de forma recursiva, repitiendo el proceso hasta que se ingrese un valor válido.
"""

def get_int():
    try:
        num = int(input("Ingrese un número entero: "))
        return num
    except ValueError:
        print("El valor ingresado no es un número entero. Intente nuevamente.")
        return get_int()

num = get_int()
print("El número ingresado es:", num)
