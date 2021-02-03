# def busca_pais(country, paisGiven):
#     """
#     paises es un diccionario. pais es la llave.
#     codigo con el principio EAFP.
#     """
#     try:
#         return paises[paisGiven]

#     except KeyError:
#           return None


pais = 'Colombia' #key

def busca_paisX(countries, pais):
    """
    Countries es un diccionario. Paris es la llave que yo le doy.
    Codigo con el principio EAFP.
    """
    
    try:
        return countries[pais]        #dict[key] //  pais turn it into a Key 
    except KeyError:
        return f'Man, el pais que buscas, no se encuentra en la base de datos'

countries = {
'España': 'Madrid', 
'Ecuador':'Quito', 
'Francia':'Paris', 
'Colombia':'Bogota'
}       

print(busca_paisX(countries, pais)) #caller with Colombia
print(busca_paisX(countries, "Mexico")) #argument stablished as Mexico should run the return