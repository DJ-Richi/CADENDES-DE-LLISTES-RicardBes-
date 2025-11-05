# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/11/2024
# Versió: 1
#
# Descripció: Fes un programa que elimini els duplicats d'una llista.
# Especificacions Programa que et elimini duplicats d'una llista.

# Llista amb duplicats
llista_original = [3, 7, 2, 6, 7, 9, 4, 5, 7, 2, 5, 3, 9]

# Eliminar duplicats convertint la llista en un conjunt i tornant-la a llista
llista_sense_duplicats = list(set(llista_original))

# Mostrar el resultat
print("Llista original:", llista_original)
print("Llista sense duplicats:", llista_sense_duplicats)