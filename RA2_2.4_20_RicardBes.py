# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 04/11/2024
# Versió: 1
#
# Descripció: Demana una llista de paraules i crea una nova llista amb només les paraules que començen per vocal.
# Especificacions Programa que fagi una llista de paraules i que crea una nova llista amb només les paraules que començen per volcal.

def comencen_per_vocal(paraules):
    vocals = 'aeiouAEIOU'
    return [p for p in paraules if p and p[0] in vocals]

# Demanar paraules a l'usuari
entrada = input("Escriu paraules separades per espais: ")
llista_paraules = entrada.split()

# Filtrar les que comencen per vocal
llista_vocals = comencen_per_vocal(llista_paraules)

# Mostrar el resultat
print("Paraules que comencen per vocal:", llista_vocals)