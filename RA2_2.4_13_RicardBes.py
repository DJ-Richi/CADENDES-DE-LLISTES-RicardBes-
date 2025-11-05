# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/11/2024
# Versió: 1
#
# Descripció: Escriu una funció que sumi tots els nombres d'una llista.
# Especificacions Programa que et sumi tots els nombres d'una llista.

# Funció que suma tots els nombres d'una llista
def suma_llista(llista):
    return sum(llista)

# Explicacio d'ús del codi
nombres = [52, 64, 54, 31, 10]
resultat = suma_llista(nombres)

print("La suma dels nombres és:", resultat)
