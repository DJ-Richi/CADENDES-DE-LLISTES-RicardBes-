# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Demana una cadena i compta quantes vegades apareix una lletra concreta.
# Especificacions Programa que et demani quantes vegades apareix una lletra concreta.

cadena = input("Introdueix una cadena: ")

lletra = input("Introdueix la lletra que vols comptar: ")

if len(lletra) != 1:
    print("Has d'introduir només una lletra.")
else:
    comptador = cadena.count(lletra)
    print(f"La lletra '{lletra}' apareix {comptador} vegada(es) a la cadena.")
