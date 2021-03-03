def funcion_decoradora(parameter):
	def wrapper():
		print("Este es el último mensaje...")
		parameter() 
		print("Este es el primer mensaje ;)")
	return wrapper()

def zumbido():
	print("Buzzzzzz")
zumbido = funcion_decoradora(zumbido)

@funcion_decoradora
def zumbido():
	print("BuXXzzzzzz")


