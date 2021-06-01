import re


# Reemplaza las vocales con tilde por vocales sin tilde
def normalizar_tildes(texto):
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazos:
        texto = texto.replace(a, b)
    return texto


# Pasa el texto a minúsculas y quita todos los caracteres que no sean letras.
# La letra 'ñ' no se contempla, es decir, también se quitará.
def normalizar_cifrado(texto):
   texto = texto.lower()
   texto = re.sub(r'[^a-z]', '', texto)
   return texto
