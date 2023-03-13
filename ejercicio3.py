def contar_palabras(cadena):
    """
    Cuenta la frecuencia de cada palabra en una cadena de caracteres y devuelve un diccionario.
    
    Primero, la función convierte la cadena de entrada a minúsculas y elimina los signos de puntuación utilizando el método replace().
    Luego, la cadena se divide en palabras utilizando el método split().
    Por último, la función cuenta la frecuencia de cada palabra utilizando un diccionario: si la palabra ya está en el diccionario, se incrementa su valor en 1; de lo contrario, se añade la palabra al diccionario con un valor inicial de 1.
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

cadena = "Hola mundo. Hola Python. Python es genial!"
frecuencia = contar_palabras(cadena)
print(frecuencia)
