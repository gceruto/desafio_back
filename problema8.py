def busqueda_recursiva(lista,numero,izq,der):
    if izq > der:
        return -1
    centro = int((izq+der)/2)
    if lista[centro] == numero:
        return centro
    elif lista[centro] > numero:
        return busqueda_recursiva(lista,numero,izq,centro-1)
    else:
        return busqueda_recursiva(lista,numero,centro+1,der)

# Retorna la posición en lista si se encuentra el numero a buscar
# y -1 si no está.
def busqueda_binaria(lista,numero):
    return busqueda_recursiva(lista,numero,0,len(lista)-1)

# Map de la lista2, usando la funcion busqueda_binaria
#  y la lista1 como dominio de búsqueda.
def map_lista(lista1, lista2):
    resultado = []
    for x in lista2:
        resultado.append(busqueda_binaria(lista1,x))
    return resultado



