#Una mañana ponés un billete en la vereda al lado del obelisco porteño. 
#A partir de ahí, cada día vas y duplicás la cantidad de billetes, 
#apilándolos prolijamente. 
#¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el obelisco?

grosor_billete = 0.11 * 0.001 # en metros
altura_obelisco = 67.5 # metros
numero_billetes = 1
dia = 1

while numero_billetes * grosor_billete <= altura_obelisco :
    print(dia, numero_billetes, numero_billetes * grosor_billete)
    dia = dia + 1
    numero_billetes = numero_billetes * 2
    
print('Cantidad de dias ', dia)
print('Cantidad de Billetes ', numero_billetes)
print('Altura final ', numero_billetes * grosor_billete)
