#David Encastin Flores Class 7
#Enzo Cardenas 
#Edwin Antonio Can


#https://pythones.net/propiedades-en-python-oop/#:~:text=%E2%80%9CAtributos%20manejables%E2%80%9D%20que%20nos%20permiten,%2Fa%2C%20borrado%2Fa

#https://pythones.net/decoradores-en-python-oop/
 
"""En Python los getters y setters tienen el objetivo de asegurar el 
encapsulamiento de datos
"""

#######    CLASE SIN SETTER Y GETTERS    #############

class Millas:
 def __init__(self, distanciaX = 0):
     self.distancia = distanciaX
     print('Distancia inicial: ', distanciaX)
     
 
 def convertirAKilomentros(self):
     return(self.distancia * 1.609344)

#Creamos un nuevo objeto
avion = Millas()

#Indicamos la distancia
avion.distancia = 200#Regresa el valor a la función "def __init__"

#Obtenemos el atributo de distancia
print('Distancia final en Millas: ',avion.distancia)   #imprime --> 200

#Obtener el método convertirAKilometros
print('Distancia final en Kilometros: ',avion.convertirAKilomentros())