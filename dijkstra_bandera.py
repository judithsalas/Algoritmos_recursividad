from collections import Counter
'''
Se ha importado del módulo collections la clase Counter.
Counter simplifica el proceso de contar las fichas por color, 
eliminando la necesidad de verificar y actualizar manualmente un diccionario.
'''
def ordenar_fichas(fichas):
    # Contar la frecuencia de cada color utilizando Counter
    frecuencia = Counter(fichas)

    # Generar la secuencia ordenada de fichas
    orden = []
    for color in ['rojo', 'verde', 'azul']:  # Esto asegura el orden rojo, verde, azul
        orden.extend([color] * frecuencia[color])

    return orden

# Pedir al usuario que ingrese las fichas
fichas = input("Ingrese las fichas separadas por espacios (rojo, verde, azul): ").split()

# Verificar si las fichas son válidas
colores_validos = {'rojo', 'verde', 'azul'}
if any(ficha not in colores_validos for ficha in fichas):
    print("Error: Las fichas ingresadas no son válidas. Por favor, ingrese solo 'rojo', 'verde' o 'azul'.")
else:
    # Ordenar las fichas
    orden = ordenar_fichas(fichas)
    print("Orden original de las fichas:", fichas)
    print("Fichas ordenadas:", orden)
