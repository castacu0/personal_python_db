students = {
  "Rumania" : "15",
  "Canada" : "1",
  "Singapur" : "29",
  "Mexico" : "4",
  }

for key, value in students.items():
    if value == "1":
        is_or_are = 'is'
        s = ""
    else: 
        is_or_are = 'are'
        s = "s"
    print(f'In {key} there {is_or_are} {value} student{s}.')

# Los diccionariones funcionan con formato ➡ "KEY":VALUE
# El diccionario se llama 'students'
# Los nombres de los paises estan del lado izquierdo, entonces son KEY
# El numero de estudiantes por pais está del lado derecho, entonces son VALUE

# OJO! 🔺  Mucha atencion en   students.items():
#   .items   me está dando libertad de usar tanto la KEY como el VALUE 
# que existen en el diccionario 'students' 
# Si no lo pongo, no jalaria todo el show de a continuacion

# Ahora si, vamos a leerlo juntos...
# PARA la variable key (tu ponle el nombre que quieras realmente. Por ejemplo: pais)
# y para la variable value (igual, la variable se puede llamar numeroDeEstudiantes o otra cosa)
# Que se encuentran en el rango del 0 al 3. Porque hay 4 valores dentro del diccionario students
# O tambien se lee, 'Que se encuentran en el rango de students'
# Con el atributo  .items():   para que lea las 2 variables que pusimos en el 'for'

# Corre lo siguiente 🛴


    #Imprime texto ordenado, para eso la  f
    #En la variable {key} estan los paises
    #En la variable {is_or_are} estan si hay 1 o mas alumnos, por eso el IS o el espacio vacio
    # Si hay mas de 1 estudiante entonces se le agrega ARE y la S al final de studentS.

    #Recuerda que el PRINT va dentro del FOR pero fuera del else.
  