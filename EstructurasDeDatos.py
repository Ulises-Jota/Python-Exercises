from Utils import normalizar_tildes
import re


# Escribir una función contar(x,y) que cuente cuántas veces aparece un carácter x dado en
# una cadena y.

def contar(x, y):
    contador = 0
    for c in y:
        if c == x:
            contador += 1
    print(f'El caracter "{x}" aparece {contador} veces')


contar('a', 'ahora a dormir')


# Escribir un programa que decida si hay más letras “A” o más letras “E” en una cadena.

def contar_a_y_e():
    frase = input("Ingrese una frase: ").lower()
    frase = normalizar_tildes(frase)
    a = frase.count('a')
    e = frase.count('e')
    if a > e:
        print(f'Hay más letras "A" ({a}) que "E" ({e})')
    elif a < e:
        print(f'Hay más letras "E" ({e}) que "A" ({a})')
    else:
        print(f'Hay la misma cantidad de letras "A" ({a}) que "E" ({e})')


contar_a_y_e()


# Escribir un programa que cuente cuantas veces aparecen cada una de las vocales en una
# cadena. No importa si la vocal aparece en mayúscula o en minúscula.

def contar_vocales():
    vocales = ('a', 'e', 'i', 'o', 'u')
    dic_cont_vocales = dict.fromkeys(vocales, 0)
    frase = input("Ingrese una frase: ").lower()
    frase = normalizar_tildes(frase)
    for letra in frase:
        if letra == 'a':
            dic_cont_vocales['a'] = dic_cont_vocales['a'] + 1
        elif letra == 'e':
            dic_cont_vocales['e'] = dic_cont_vocales['e'] + 1
        elif letra == 'i':
            dic_cont_vocales['i'] = dic_cont_vocales['i'] + 1
        elif letra == 'o':
            dic_cont_vocales['o'] = dic_cont_vocales['o'] + 1
        elif letra == 'u':
            dic_cont_vocales['u'] = dic_cont_vocales['u'] + 1

    print(f"""Se contaron las siguientes cantidades de vocales:

    'A' = {dic_cont_vocales['a']}
    'E' = {dic_cont_vocales['e']}
    'I' = {dic_cont_vocales['i']}
    'O' = {dic_cont_vocales['o']}
    'U' = {dic_cont_vocales['u']}""")


contar_vocales()


# Escribir una función que reciba como parámetro una cadena de palabras separadas por
# espacios y devuelva, como resultado, cuántas palabras de más de cinco letras tiene la
# cadena dada.

def mas_de_cinco(str):
    contador = 0
    palabras = str.split()
    for palabra in palabras:
        if len(palabra) > 5:
            contador += 1
    return contador


frase = input("Ingrese una frase: ")
print(f'La frase "{frase}" tiene {mas_de_cinco(frase)} palabras con más de 5 letras.')


# Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo de su
# oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando
# que una palabra fue cortada con el agregado de una arroba). Por otro lado cobra un valor
# para las palabras cortas y otro valor para las palabras largas (que deben ser cortadas).
# Escribir una función que reciba un texto, la longitud máxima de las palabras, el costo de
# cada palabra corta, el costo de cada palabra larga, y devuelva como resultado el texto del
# telegrama y el costo del mismo.

# Toma en cuenta los signos de puntuación para no cobrar extra, calcula la longitud de cada palabra
# y si tiene más de 5 letras, toma las primeras 5 y le concatena un '@'. Va contando las palabras,
# sean largas o cortas, y luego calcula el costo en base a las cantidades.
def escribir_telegrama(mensaje, long_max, costo_palabra_corta, costo_palabra_larga):
    contador_largas = 0
    contador_cortas = 0
    lista_palabras = mensaje.split()
    for index, palabra in enumerate(lista_palabras):
        match = re.search(r'([^\w])', palabra)
        if match:
            signo_puntuacion = match.group()
            lista_palabras[index] = palabra.replace(signo_puntuacion, '')
        else:
            signo_puntuacion = ''
        if len(palabra) > long_max:
            lista_palabras[index] = palabra.replace(palabra[long_max:], f"@{signo_puntuacion}")
            contador_largas+=1
        else:
            contador_cortas+=1

    mensaje = " ".join(lista_palabras)
    costo_telegrama = (contador_cortas * costo_palabra_corta) + (contador_largas * costo_palabra_larga)
    return f"""Mensaje: "{mensaje}"
Costo total del mensaje: {costo_telegrama} pesos"""


telegrama = input("Ingrese el mensaje: ")
longitud = int(input("Ingrese la longitud máxima por palabra: "))
costo_corta = int(input("Ingrese el costo de una palabra corta: "))
costo_larga = int(input("Ingrese el costo de una palabra larga: "))

print(escribir_telegrama(telegrama, longitud, costo_corta, costo_larga))


# Implementar un diccionario Inglés – Español, permitiendo agregar una palabra en inglés
# y su traducción al español, consultar la traducción de una palabra en ambos sentidos
# (inglés a español y español a inglés) contar la cantidad de palabras y mostrar el
# diccionario ordenado de la Z a la A.

dic_eng_spa = {}

def agregar_palabra():
    eng_word = input("Ingrese la palabra en inglés: ").lower()
    spa_word = input("Ingrese su traducción al español: ").lower()
    dic_eng_spa[eng_word] = spa_word
    return dic_eng_spa

def consultar_palabra():
    palabra_buscada = input("Ingrese la palabra que busca: ").lower()
    for key, value in dic_eng_spa.items():
        if palabra_buscada == value:
            print(f'La palabra "{palabra_buscada}" se traduce como "{key}"')
        elif palabra_buscada == key:
            print(f'La palabra "{palabra_buscada}" se traduce como "{value}"')

def contar_palabras():
    print(f'El diccionario tiene {len(dic_eng_spa)} palabras')

def ordenar_descendente():
    return sorted(dic_eng_spa.keys(), reverse=True)


seguir_buscando = 'SI'
while seguir_buscando == 'SI':
    agregar_palabra()
    seguir_buscando = str(input("¿Desea agregar otra palabra? ")).upper()

consultar_palabra()

contar_palabras()

print(ordenar_descendente())


# Implementar una lista de precios que permita grabar el precio de un producto, consultar
# el precio de un producto, consultar todos los productos cuyo precio sea mayor a un valor
# ingresado y mostrar los productos ordenados del más barato al más caro.

lista_precios = {}

def grabar_precio():
    precio = int(input("Ingrese el precio del producto: "))
    producto = input("Ingrese el producto: ").lower()
    lista_precios[producto] = precio
    return lista_precios


def consultar_precio():
    producto = input("Ingrese el producto del que quiere saber el precio: ").lower()
    print(f'El producto "{producto}" tiene un precio de {lista_precios[producto]} pesos')


def consultar_productos():
    prod_consultados = {}
    precio_minimo = int(input("Ingrese el precio mínimo de los productos a consultar: "))
    for producto, precio in lista_precios.items():
        if precio >= precio_minimo:
            prod_consultados[producto] = precio
    print(sorted(prod_consultados.items(), reverse=True))


seguir_grabando = 'SI'
while seguir_grabando == 'SI':
    grabar_precio()
    seguir_grabando = str(input("¿Desea agregar otro producto? ")).upper()

consultar_precio()

consultar_productos()
