# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Escriu una funció que reverteixi una cadena.
# Especificacions Programa que una funció reverteixi una cadena.

paraula = input("Introdueix una paraula: ")

if paraula == paraula[::-1]:
    print("És un palíndrom.")
else:
    print("No és un palíndrom.")
