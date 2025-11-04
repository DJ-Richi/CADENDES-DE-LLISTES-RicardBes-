# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Escriu una funció que reverteixi una cadena.
# Especificacions Programa que una funció reverteixi una cadena.

def reverteix_cadena(cadena):
    return cadena[::-1]

text = input("Introdueix una cadena: ")
print("Cadena invertida:", reverteix_cadena(text))
