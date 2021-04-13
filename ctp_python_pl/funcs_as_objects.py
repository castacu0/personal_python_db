# def multiplicar_por_dos(n):
#     return n * 2

# def sumar_dos(n):
#     return n + 2

# def aplicar_operacion(f, numeros):
#     resultados = []
#     for each_numero in numeros:
#         resultado = f(each_numero)
#         resultados.append(resultado)
#     return resultado

# nums = [1, 2, 3]

# aplicar_operacion(multiplicar_por_dos, nums) #CALLER
# print(aplicar_operacion(multiplicar_por_dos, nums))
# #>>> [2, 4, 6]

# aplicar_operacion(sumar_dos, nums) #CALLER 
# print(aplicar_operacion(sumar_dos, nums))
# #>>> [3, 4, 5]

def aplicar_operaciones(num): #1 parameter
    operaciones = [abs, float, str] #list
 
    resultado = [] #you will save the return

    for each_operacion in operaciones:
        resultado.append(each_operacion(num))

    return resultado

print(aplicar_operaciones(-1))