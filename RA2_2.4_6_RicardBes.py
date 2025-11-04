# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Demana una cadena i mostra la primera i l'última lletra.
# Especificacions Programa que una cadena mostri la primera i ultima lletra.

cadena = input("Introdueix una cadena: ")

if len(cadena) > 0:
    print("Primera lletra:", cadena[0])
    print("Última lletra:", cadena[-1])
else:
    print("Has introduït una cadena buida.")
