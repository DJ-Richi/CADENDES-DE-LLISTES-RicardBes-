# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/11/2024
# Versió: 1
#
# Descripció: Demana a l'usuari 5 paraules i emmagatzema-les en una llista.
# Especificacions Programa que et demani 5 paraules i que les emmagatzema en una llista.

paraules = []

for i in range(5):
    paraula = input("Introdueix una paraula: ")
    paraules.append(paraula)

print("Les paraules introduides son:", paraules)