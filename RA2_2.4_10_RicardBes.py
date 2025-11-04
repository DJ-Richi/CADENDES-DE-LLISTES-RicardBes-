# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Fes un script que concateni dues cadenes separades per un guió "-".
# Especificacions Programa que et fagi un script de dues cadenes.

def concatena_cadenes(cadena1, cadena2):
    return cadena1 + "-" + cadena2

text1 = "Barcelona"
text2 = "Catalunya"

resultat = concatena_cadenes(text1, text2)
print("Resultat:", resultat)