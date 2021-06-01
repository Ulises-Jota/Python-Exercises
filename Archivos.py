import csv
import re


# 1. Escribir un programa que lea la información de vacunación por COVID-19 por provincias y
# almacene en estructuras que permitan dar respuestas a las siguientes consultas:
#     1. Dada una provincia informar total de vacunas aplicadas, tipo de vacuna con mayor
#     cantidad de aplicaciones, tipo de vacuna con menor cantidad de aplicaciones.
#     2. Listar un ranking de las 10 provincias con mayor porcentaje de segundas dosis
#     totales aplicadas
#     3. Listar un ranking de las vacunas por mayor porcentaje de segundas dosis totales
#     aplicadas

# Filtra las filas del dictReader según 'jurisdiccion_nombre'
def filtro_provincia(provincia, dict_reader_vacunas):
    return filter(lambda row: row['jurisdiccion_nombre'] == provincia, dict_reader_vacunas)


# Recorre el dictReader filtrado y extrae una lista de tuplas en la forma (Nombre vacuna, Cantidad de dosis).
# La cantidad de dosis surge de sumar la primera más la segunda dosis de cada línea.
# Obtiene la suma total de las dosis. Luego ordena la lista según la cantidad de vacunas, y toma el primer nombre como
# el nombre de la vacuna con el máximo de dosis, y el último nombre como el nombre con el mínimo de dosis.
def info_vacunas_aplicadas(dic_vacunas_filtrado):
    lista_info_vacunas = [(row['vacuna_nombre'], int(row['primera_dosis_cantidad']) + int(row['segunda_dosis_cantidad']))
                          for row in dic_vacunas_filtrado]
    total_vacunas = sum([cantidad_vacunas for nombre_vacuna, cantidad_vacunas in lista_info_vacunas])
    lista_info_vacunas = sorted(lista_info_vacunas, key=lambda x: x[1])
    max_vacunas = lista_info_vacunas[-1][0]
    min_vacunas = lista_info_vacunas[0][0]
    return total_vacunas, max_vacunas, min_vacunas


def vacunas_por_provincia():
    provincia = input("Ingrese la provincia por la que desea consultar: ")
    with open('Covid19VacunasAgrupadas.csv', newline='') as csv_vacunas:
        dict_reader_vacunas = csv.DictReader(csv_vacunas)
        dic_vacunas_filtrado = filtro_provincia(provincia, dict_reader_vacunas)
        total_vacunas, max_vacunas, min_vacunas = info_vacunas_aplicadas(dic_vacunas_filtrado)
        print("""
        Total de vacunas aplicadas: {0}
        Vacuna con la mayor cantidad de aplicaciones: {1}
        Vacuna con la menor cantidad de aplicaciones: {2}""".format(
            total_vacunas, max_vacunas, min_vacunas
        ))


# Recorre el objeto dictReader, obteniendo las provincias (o las vacunas) y las segundas dosis.
# Retorna el diccinario resultante.
def ranking(valor):
    dic_ranking = {}
    with open('Covid19VacunasAgrupadas.csv', newline='') as csv_vacunas:
        dict_reader_vacunas = csv.DictReader(csv_vacunas)
        for row in dict_reader_vacunas:
            if row[valor] in dic_ranking.keys():
                dic_ranking[row[valor]] += int(row['segunda_dosis_cantidad'])
            else:
                dic_ranking[row[valor]] = int(row['segunda_dosis_cantidad'])
    return dic_ranking


# Main program
vacunas_por_provincia()

print()

valor = input("""Por favor, ingrese la variable de la que quiere obtener el ranking:
    1: Ranking por Provincia
    2: Ranking por Tipo de vacuna
    Cualquier otra tecla: Salir
    """)
if valor == '1':
    valor = 'jurisdiccion_nombre'
    dic_tipo_ranking = ranking(valor)
    # Ordena de mayor a menor según cantidad de vacunas por provincia y toma las primeras 10 tuplas.
    print(f'Las 10 provincias con la mayor cantidad de segundas dosis son (ordenadas de mayor a menor):')
    for provincia in sorted(dic_tipo_ranking.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f'{provincia[0]}: {provincia[1]}')
elif valor == '2':
    valor = 'vacuna_nombre'
    dic_tipo_ranking = ranking(valor)
    # Ordena de mayor a menor según cantidad de vacunas por tipo de vacuna.
    print(f'Las vacunas con la mayor cantidad de segundas dosis son (ordenadas de mayor a menor):')
    for vacuna in sorted(dic_tipo_ranking.items(), key=lambda x: x[1], reverse=True):
        print(f'{vacuna[0]}: {vacuna[1]}')
else:
    pass



# 2. Escribir un programa que lea un archivo de texto y escriba en otro archivo, una lista con
# las 10 palabras con mayor ocurrencia ordenadas por cantidad de ocurrencias, tener en
# cuenta una lista de palabras ignoradas en el análisis de ocurrencias.

lista_palabras_ignoradas = ('es', 'el', 'la', 'de', 'las', 'los', 'un', 'una', 'uno', 'se')
dic_palabras_ocurrencias = {}

nombre_archivo_entrada = 'Lorem Ipsum.txt'
nombre_archivo_salida = 'Lorem Ipsum - Palabras.txt'


# Abre el archivo de texto y lo lee.
# Procesa línea por línea para quitar todos los caracteres que no sean letras
# y las divide por espacio para obtener una lista de palabras.
# Obtiene las palabras, ignorando las de la lista de palabras ignoradas,
# y las guarda en un diccionario que luego retorna.
def obtener_palabras():
    with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.lower()
            linea = re.sub('[^a-záéíóúñ\\s]', '', linea)
            lista_palabras_linea = linea.split()
            for palabra in lista_palabras_linea:
                if palabra in lista_palabras_ignoradas:
                    continue
                elif palabra in dic_palabras_ocurrencias.keys():
                    dic_palabras_ocurrencias[palabra] += 1
                else:
                    dic_palabras_ocurrencias[palabra] = 1
        return dic_palabras_ocurrencias


# Se le pasa por parámetro la función obtener_palabras(). Al diccionario que retorna,
# lo convierte en una lista de tuplas que ordena según las cantidades de ocurrencias, de mayor a menor.
# Toma las primeras 10 tuplas y las escribe en otro archivo de texto.
def escribir_palabras(funcion):
    lista_palabras_ocurrencias = sorted(funcion.items(), key=lambda x: x[1], reverse=True)[:10]
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo:
        for palabra, ocurrencias in lista_palabras_ocurrencias:
            archivo.write(f'{palabra}: {str(ocurrencias)}\n')


# Main program
escribir_palabras(obtener_palabras())
