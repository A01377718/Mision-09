# encoding: UTF-8
# Misión 9
# Javier Alexandro Vargas Sánchez
# Programa que realiza diversas funciones con listas
from math import sqrt
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def extraerPares(lista):  #hace una lista solo con los numeros pares de la lista ya dada

    listaPares = []

    for numero in lista:

        valor = numero % 2

        if valor == 0:
            listaPares.append(numero)
        else:
            pass

    return listaPares
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def extraerMayoresPrevio(lista):  # Dada una lista, elimina el primer y el último valor de la lista
    listaMayores = []

    for numero in range(1, len(lista)):
        if lista[numero] > lista[numero - 1]:
            listaMayores.append(lista[numero])


    return listaMayores
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def intercambiarParejas(lista):  #intercambia la posión de cada dato en las parejas,
    # si el numero de datos de la lista es impar, la úlima pareja no cambia

    # par
    listaIntercambiada = []

    par = False

    if len(lista) % 2 == 0:
        par = True

    if par == False:

        for numero in range(0, len(lista) - 1, 2):
            listaIntercambiada.append(lista[numero + 1])
            listaIntercambiada.append(lista[numero])
        listaIntercambiada.append(lista[- 1])

    elif par == True:

        for numero in range(0, len(lista), 2):
            listaIntercambiada.append(lista[numero + 1])
            listaIntercambiada.append(lista[numero])

    return listaIntercambiada


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def intercambiarMM(lista):#el numero mayor y menor de la lista intercambian posiciones
    if len(lista) == 0:
        return lista
    else:

        maximo = max(lista) #Numero mayor de la lista
        minimo = min(lista) #Numero menor de la lista

        posicionMax = lista.index(maximo) #Indice del valor mayor en la lista
        posicionMin = lista.index(minimo) #Indice del valor menor en la lista

        lista[posicionMax] = minimo #Intercambio
        lista[posicionMin] = maximo

        return lista

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def promediarCentro(lista):#calcula el promedio de una lista desestimando el valor máximo y mínimo
    if len(lista)<= 2:
        return 0

    else:
        lista.sort()
        lista.pop()
        lista.pop(0)

        promedio = sum(lista)//len(lista)

        return promedio

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def calcularEstadistica(lista): #calcula el promedio y la desviación estándar de una lista

    dato = (0,0)

    if len(lista) == 0:
        return dato

    else:
        cuadDist = []

        promedio = sum(lista)/len(lista)

        for numero in lista:

            distancia = (numero - media) ** 2

            cuadDist.append(distancia)

        media2 = sum(cuadDist)/(len(lista)-1)

        desviacionEstandar = sqrt(media2)

        #dato = (promedio, '%.6f' % desviacionEstandar)

        dato= (promedio, desviacionEstandar)

        return dato


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main():
    # -----------------------------------------------------------------------------------------------Pruebas Ejercicio 1
    listaEj1A = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaEj1B = []
    listaEj1C = [5, 7, 3]

    # -----------------------------------------------------------------------------------------------Pruebas Ejercicio 2
    listaEj2A = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaEj2B = [5, 4, 3, 2]
    listaEj2C = []

    # -----------------------------------------------------------------------------------------------Pruebas Ejercicio 3
    listaEj3A = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    listaEj3B = [1, 2, 3]
    listaEj3C = [7]
    listaEj3D = []

    # ------------------------------------------------------------------------------------------------Pruebas Ejericio 4
    listaEj4A = [5, 9, 3, 22, 19, 31, 10, 7]
    listaEj4Acopia = [5, 9, 3, 22, 19, 31, 10, 7]
    listaEj4B = [1, 2, 3]
    listaEj4Bcopia = [1, 2, 3]
    listaEj4C = []

    # -----------------------------------------------------------------------------------------------Pruebas Ejercicio 5
    listaEj5A = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    listaEj5Acopia= [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    listaEj5B = [70, 80, 90]
    listaEj5Bcopia = [70, 80, 90]
    listaEj5C = [20, 55, 30, 5, 55, 5]
    listaEj5Ccopia =[20, 55, 30, 5, 55, 5]
    listaEj5D = [5,9,1,8]
    listaEj5Dcopia =[5,9,1,8]
    listaEj5E = [5,8]

    # -----------------------------------------------------------------------------------------------Pruebas Ejercicio 6
    listaEj6A = [1,2,3,4,5,6]
    listaEj6B = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    listaEj6C = []

    ####################################################################################################################
    print("Ejercicio 1:")
    print("La lista", listaEj1A, "regresa la lista con solo pares", extraerPares(listaEj1A))
    print("La lista", listaEj1B, "regresa la lista con solo pares", extraerPares(listaEj1B))
    print("La lista", listaEj1C, "regresa la lista con solo pares", extraerPares(listaEj1C))
    print()

    ####################################################################################################################
    print("Ejercicio 2:")
    print("La lista original", listaEj2A, ", regresa", extraerMayoresPrevio(listaEj2A))
    print("La lista original", listaEj2B, ", regresa", extraerMayoresPrevio(listaEj2B))
    print("La lista original", listaEj2C, ", regresa", extraerMayoresPrevio(listaEj2C))
    print()

    ####################################################################################################################
    print("Ejercicio 3:")
    print("La lista", listaEj3A, ", regresa así", intercambiarParejas(listaEj3A))
    print("La lista", listaEj3B, ", regresa así", intercambiarParejas(listaEj3B))
    print("La lista", listaEj3C, ", regresa así", intercambiarParejas(listaEj3C))
    print("La lista", listaEj3D, ", regresa así", intercambiarParejas(listaEj3D))
    print()

    ####################################################################################################################
    print("Ejercicio 4:")
    print("La lista", listaEj4Acopia, ", regresa así", intercambiarMM(listaEj4A))
    print("La lista", listaEj4Bcopia, ", regresa así", intercambiarMM(listaEj4B))
    print("La lista", listaEj4C, ", regresa así", intercambiarMM(listaEj4C))
    print()

    ####################################################################################################################
    print("Ejercicio 5:")
    print("La lista", listaEj5Acopia, "regresa este promedio", promediarCentro(listaEj5A))
    print("La lista", listaEj5Bcopia, "regresa este promedio", promediarCentro(listaEj5B))
    print("La lista", listaEj5Ccopia, "regresa este promedio", promediarCentro(listaEj5C))
    print("La lista", listaEj5Dcopia, "regresa este promedio", promediarCentro(listaEj5D))
    print("La lista", listaEj5E, "regresa este promedio", promediarCentro(listaEj5E))
    print()

    ####################################################################################################################
    print("Ejercicio 6:")
    print("La media y desviación estándar de la lista", listaEj6A, "es", calcularEstadistica(listaEj6A))
    print("La media y desviación estándar de la lista", listaEj6B, "es", calcularEstadistica(listaEj6B))
    print("La media y desviación estándar de la lista", listaEj6C, "es", calcularEstadistica(listaEj6C))
    print()
    ####################################################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



main()
