# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Escriu una funció que elimini tots els espais d'una cadena.
# Especificacions Programa que et elimini tots els espais d'una cadena.

def elimina_espais(cadena):
    """
    Esta funció rep una cadena de text i retorna la mateixa cadena
    sense ningun espai en blanc.
    """
    return cadena.replace(" ", "")

text_original = "Hola món, com estàs?"
text_sense_espais = elimina_espais(text_original)

print("Text original:", text_original)
print("Text sense espais:", text_sense_espais)

