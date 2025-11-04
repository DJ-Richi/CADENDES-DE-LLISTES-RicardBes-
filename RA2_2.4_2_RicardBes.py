# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Demana una frase i compta quantes vocals conté.
# Especificacions Programa que una frase compti les vocals que conté.

frase = input("Introdueix una frase: ")

vocals = "aeiouAEIOU"

comptador = 0

for lletra in frase:
    if lletra in vocals:
        comptador += 1

print("La frase conté", comptador, "vocal(s).")
