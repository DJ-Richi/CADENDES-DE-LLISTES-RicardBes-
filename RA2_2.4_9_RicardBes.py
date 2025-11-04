# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Crea un programa que divideixi una frase en paraules i les mostri una per una.
# Especificacions Programa que et divideixi una frase en paraules.

def mostra_paraules(frase):
    """
    Esta funció rep una frase i imprimeix cada paraula en una línia separada.
    """
    paraules = frase.split()
    for paraula in paraules:
        print(paraula)

frase = "El sol brilla sobre el riu"
mostra_paraules(frase)