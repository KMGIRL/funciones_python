# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función ordenar
#def ordenar (numeros):


# --------------------------------






def ordenar(numeros):
    ordenados= sorted(numeros)
    return ordenados



    # Alumno: Crear la función "ordenar"

    # Generar una una nueva funcion que se llame "ordenar",
    # que utilizaremos para odernar la lista de numeros.
    # Debe recibir 1 parámetro que es la lista de números
    # y retornar la nueva lista ordenada (muy simular a la función promedio)

    # Dentro de la función puede ordenar la lista
    # usando la funciones nativas de Python "sort"

    # Luego de crear la función invocarla en este lugar:

numeros=[5,2,3,8,10,9]    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python") 

    orden= ordenar(numeros)


    print('los nros ordenados:', orden)

   

    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar:

print("terminamos")
