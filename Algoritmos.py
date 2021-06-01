import Utils


lista_numeros = [3, 8, 9, 11, 12, 1, 4, 92, 45, 33, 88, 55, 5]
print(f'Lista de números original: {lista_numeros}.')


# 1. Implementar un algoritmo de ordenamiento por burbuja de una lista numérica.

# Recorre la lista comparando el elemento actual con el anterior.
# En caso de que sea menor, realiza el intercambio.
def ordenamiento_burbuja(lista):
    for repeticion in range(len(lista) - 1):
        for index in range(len(lista) - 1):
            if lista[index + 1] < lista[index]:
                lista[index + 1], lista[index] = lista[index], lista[index + 1]
    return lista


# Main program
print(f'El ordenamiento por burbuja queda: {ordenamiento_burbuja(lista_numeros)}.')


# 2. Implementar un algoritmo de ordenamiento por inserción de una lista numérica.

# Mientras el elemento actual sea menor al elemento anterior,
# y mientras no haya llegado al primer elemento de la lista,
# realiza el intercambio, "retrocede" y repite la comparación.
# Si no encuentra un elemento menor, prosigue con el próximo elemento de la lista.
def ordenamiento_insercion(lista):
    for index_elem_actual in range(1, len(lista)):
        index_elem_anterior = index_elem_actual - 1
        while lista[index_elem_actual] < lista[index_elem_anterior] and index_elem_anterior >= 0:
            lista[index_elem_actual], lista[index_elem_anterior] = lista[index_elem_anterior], lista[index_elem_actual]
            index_elem_actual -= 1
            index_elem_anterior -= 1
    return lista


# Main program
print(f'El ordenamiento por inserción queda: {ordenamiento_insercion(lista_numeros)}')


# 3. Implementar los algoritmos de búsqueda simple y binaria.
#     1. Búsqueda simple: busca desde el primer dato hasta el último, uno a uno comparando
# sucesivamente todos los datos en memoria hasta localizar el dato que queramos
# localizar. Este algoritmo puede usarse en cualquier situación, pero se recomienda
# usarlo solo en listas que no estén ordenadas
#     2. Búsqueda binaria: este tipo de búsqueda es usado en listas que estén previamente
# ordenadas, ya que su método de búsqueda es la de dividir los datos en dos grupos,
# eligiendo el grupo en el cual debería estar el dato buscado (supone que está
# ordenado alfabéticamente o numéricamente), volviendo a aplicar la división, y así
# sucesivamente hasta verificar si existe o no existe el dato buscado. Aplicar en este
# caso recursividad.

dato_buscado = 92


def busqueda_simple(lista, dato_buscado):
    for indice, elemento in enumerate(lista):
        if elemento == dato_buscado:
            return indice + 1


# Main program 3.1
print(f'El elemento {dato_buscado} se encuentra en la posición {busqueda_simple(lista_numeros, dato_buscado)}')


def busqueda_binaria(lista, dato_buscado):
    global apuntador_izq, apuntador_der
    apuntador_medio = int((apuntador_izq + apuntador_der) / 2)
    if dato_buscado == lista[apuntador_medio]:
        return f'El elemento {dato_buscado} se encuentra en la posición {apuntador_medio + 1}'
    elif dato_buscado > lista[apuntador_medio]:
        apuntador_izq = apuntador_medio + 1
    elif dato_buscado < lista[apuntador_medio]:
        apuntador_der = apuntador_medio - 1

    if apuntador_medio != apuntador_der and apuntador_medio != apuntador_izq:
        return busqueda_binaria(lista, dato_buscado)
    else:
        return 'El elemento no pudo ser encontrado'


# Main program 3.2
lista_ordenada = ordenamiento_insercion(lista_numeros)
apuntador_izq = 0
apuntador_der = len(lista_ordenada) - 1
print(f'Lista ordenada: {lista_ordenada}')
print(busqueda_binaria(lista_ordenada, dato_buscado))



# 4. Diseñar e implementar un algoritmo de cifrado de textos

# Implementación de un cifrado de un texto basado en el algoritmo de Vigenere
texto_original = 'Estoy en camino. No me esperen.'
print(f'Texto original: {texto_original}')


# Pasa el caracter a minúsculas, obtiene su código UNICODE
# y calcula el desplazamiento restándole 97 (código UNICODE para el caracter 'a')
def desplazamiento(caracter):
    return ord(caracter.lower()) - 97


# Recibe el texto normalizado y lo recorre para cifrar cada caracter,
# según el desplazamiento que determina la clave.
# Se utiliza el modulo en dos ocasiones: para los casos en que la letra más el desplazamiento haga que
# se supere la letra 'z', en cuyo caso debe volver a empezar desde la 'a'. Y también para el índice de
# la clave según su longitud, ya que así se va ciclando la clave sobre el texto a cifrar.
def cifrar_texto(texto, clave):
    texto_cifrado = ''
    for indice in range(len(texto)):
        texto_cifrado += chr((ord(texto[indice]) + desplazamiento(clave[indice % len(clave)]) - 97) % 26 + 97)
    return texto_cifrado


# Recibe el texto cifrado y hace lo mismo que la función de cifrado, con la excepción
# de que resta el desplazamiento según la letra de la clave asociada para obtener el texto original.
def descifrar_texto(texto, clave):
    texto_descifrado = ''
    for indice in range(len(texto)):
        texto_descifrado += chr((ord(texto[indice]) - desplazamiento(clave[indice % len(clave)]) - 97) % 26 + 97)
    return texto_descifrado


# Main program
texto_normalizado = Utils.normalizar_tildes(texto_original)
texto_normalizado = Utils.normalizar_cifrado(texto_normalizado)
print(f'Texto normalizado: {texto_normalizado}')
texto_cifrado = cifrar_texto(texto_normalizado, "COCA")
print(f'Texto cifrado:     {texto_cifrado}')
texto_descifrado = descifrar_texto(texto_cifrado, "COCA")
print(f'Texto descifrado:  {texto_descifrado}')
