# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 05/11/2024
# Versió: 1
#
# Descripció: Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.
# Especificacions Programa que et demani 10 numeros i crear 2 llistes una amb numeros parells i l'altra amb senars.

# Llistes buides per als parells i senars
parells = []
senars = []

# Demanar 10 números a l'usuari
for i in range(10):
    num = int(input("Introdueix el número: "))
    if num % 2 == 0:
        parells.append(num)
    else:
        senars.append(num)

# Mostrar les dues llistes
print("Nombres parells:", parells)
print("Nombres senars:", senars)
