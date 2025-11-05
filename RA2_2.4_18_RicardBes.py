# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Escriu una funció que retorni la llista al revés (sense reverse()).
# Especificacions Programa que escribeixi una funcio que retorni la llista del revers.

def invertir_llista(llista):
    llista_invertida = []
    for element in llista:
        llista_invertida = [element] + llista_invertida
    return llista_invertida

# Exemple d'ús
original = [1, 2, 3, 4, 5]
print(invertir_llista(original))
# Sortida: [5, 4, 3, 2, 1]
