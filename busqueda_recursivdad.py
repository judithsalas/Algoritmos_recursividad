def buscar_elemento(lista_numeros, elemento, inicio=0, final=None):
    """
    Realiza una búsqueda binaria recursiva para encontrar un elemento en una lista ordenada.

    Args:
        lista_numeros (list): La lista ordenada de números.
        elemento (int): El elemento que se desea buscar en la lista.
        inicio (int, optional): Índice de inicio para la búsqueda. Por defecto es 0.
        final (int, optional): Índice final para la búsqueda. Por defecto es None, lo que significa que se usa el último índice de la lista.

    Returns:
        int: El índice del elemento si se encuentra, -1 si no se encuentra.
    """
    if final is None:
        final = len(lista_numeros) - 1
    
    if inicio > final:
        return -1  # Elemento no encontrado
    
    medio = (inicio + final) // 2
    
    if lista_numeros[medio] == elemento:
        return medio
    elif lista_numeros[medio] < elemento:
        return buscar_elemento(lista_numeros, elemento, medio + 1, final)
    else:
        return buscar_elemento(lista_numeros, elemento, inicio, medio - 1)

# Pedir al usuario que ingrese la lista y el elemento a buscar
lista_numeros = input("Ingrese la lista ordenada de números separados por espacios: ").split()
lista_numeros = [int(x) for x in lista_numeros]  # Convertir los elementos de la lista a enteros
elemento_buscar = int(input("Ingrese el elemento que desea buscar en la lista: "))

# Verificar si la lista está ordenada
if lista_numeros != sorted(lista_numeros):
    print("Error: La lista ingresada no está ordenada.")
else:
    # Realizar la búsqueda binaria recursiva
    indice = buscar_elemento(lista_numeros, elemento_buscar)
    if indice != -1:
        print(f"El elemento {elemento_buscar} se encuentra en el índice {indice}.")
    else:
        print(f"El elemento {elemento_buscar} no se encuentra en la lista.")
