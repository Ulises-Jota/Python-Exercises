import math
import re

# 1. Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un
# cilindro usando la primera función.

def area_circulo(radio):
    return math.pi * radio * radio


def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura


print(f'El volumen de un cilindro con radio 2 y altura 8 es {volumen_cilindro(2, 8)}')


# 2. Escribir una función que reciba una muestra de números en una lista y devuelva su
# media.

def calcular_media(lista):
    return math.fsum(lista) / len(lista)


print(calcular_media([1, 5, 8, 12, 90,3]))


# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
# cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario
# generado con la función anterior y devuelva una tupla con la palabra más repetida y su
# frecuencia.

dic_palabras = {}

# Por cada palabra del texto, saca los signos de puntuación (si tiene) para contarlas después
def frecuencia_palabras(texto):
    for palabra in texto.lower().split():
        palabra = re.sub(r'[^\w]', '', palabra)
        if palabra in dic_palabras.keys():
            dic_palabras[palabra] += 1
        else:
            dic_palabras[palabra] = 1
    return dic_palabras


# Obtiene una lista de tuplas ordenadas de mayor a menor según los valores, y retorna la primera.
def palabra_mas_repetida(diccionario):
    lista_ordenada = sorted(diccionario.items(), key=lambda x:x[1], reverse=True)
    return lista_ordenada[0]


print(palabra_mas_repetida(frecuencia_palabras('¿Está listo listo? No sé. Ahora me fijo si está listo y lo saco del horno.')))


# 4. Escribir una función que reciba otra función y una lista, y devuelva otra lista con el
# resultado de aplicar la función dada a cada uno de los elementos de la lista.

# Retorna el valor pasado por argumento al cuadrado
def al_cuadrado(valor):
    return valor * valor


def aplicar_cuadrados(funcion, lista_numeros):
    return [funcion(valor) for valor in lista_numeros]


print(aplicar_cuadrados(al_cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 5. Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con
# los elementos de la lista que devuelvan True al aplicarles la función booleana.

def es_par(valor):
    return valor % 2 == 0


def obtener_pares(funcion, lista_numeros):
    return [valor for valor in lista_numeros if funcion(valor)]


print(obtener_pares(es_par, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
