numUser = int(input(f'\nEscoge un numero: '))
almostZero = 0.1 #a positive quantity close to zero.
numGuesses = 0
i = 0.0
# jump = 0.01 #almostZero**2
# jump = almostZero**2 ; print(f'Guardamos otro numero, {jump} en otra variable llamada paso')
# respuesta = 0.0 ; print(f'Guardamos la flotante {respuesta} en una variable llamada respuesta')
print()
# jump = almostZero**2

      #I chose num 4
      # while abs(  0  -  4  )  >=   0.1      and 0 <= 4
      # while         4         >=   0.1      and 0 <= 4
while abs(i**2 - numUser) >= almostZero and i <= numUser:
    #print(abs(i**2 - numUser), i)
    # i += jump
    i += jump
    numGuesses += 1
    print(f"numGuesses = {numGuesses}")

if abs(i**2 - numUser) >= almostZero:
    print(f'No se encontro la raiz cuadrada de: {numUser}')
    
else:
    answer = round(i, 6) 
    print(f'\n --> The square root of {numUser} is close to: {answer} ')