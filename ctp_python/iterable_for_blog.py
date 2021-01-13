diccionario = {
    'Rubi' : 'los Chitos',
    'Ismael' : 'la Pizza',
    'Perla' : 'los Sancochos',
    'Migue' : 'el Arroz con Pollo',
    'Enrique' : 'el Arroz con Berenjena'
    }
#Imprimir una frase que incluya la llave y el valor
for nombre, comida in diccionario.items(): #nombre y comida fueron variables creadas DENTRO del for
        # que va a correr en diccionario.items
    if comida[-1:] == 's': #Si el ultimo index y caracter de alguna de las comidas termina en S, pongale Gustan 
        singular_o_plural = 'gustan'
    else:
        singular_o_plural = 'gusta'
    print(f'A {nombre} le {singular_o_plural} {comida}.')