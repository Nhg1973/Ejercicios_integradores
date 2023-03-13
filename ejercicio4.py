def contar_palabras(cadena):
    """
    Cuenta la frecuencia de cada palabra en una cadena de caracteres y devuelve un diccionario.
    """
    # Eliminar los signos de puntuación y convertir a minúsculas
    cadena = cadena.lower()
    for signo in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
        cadena = cadena.replace(signo, " ")

    # Dividir la cadena en palabras y contar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in cadena.split():
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


def palabra_mas_repetida(frecuencia):
    """
    Devuelve una tupla con la palabra más repetida y su frecuencia en un diccionario de frecuencias.

    La función recorre el diccionario de frecuencias y va guardando la palabra que tiene la frecuencia más alta en la variable palabra_max y la frecuencia máxima en la variable frecuencia_max.
    Finalmente, la función devuelve una tupla con la palabra más repetida y su frecuencia.
    """
    palabra_max = None
    frecuencia_max = 0
    for palabra, freq in frecuencia.items():
        if freq > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = freq
    return (palabra_max, frecuencia_max)

cadena = "Hola mundo. Hola Python. Python es genial!"
frecuencia = contar_palabras(cadena)
palabra_max, frecuencia_max = palabra_mas_repetida(frecuencia)
print("La palabra más repetida es", palabra_max, "con una frecuencia de", frecuencia_max)

