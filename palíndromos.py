def verificar_palindromo(cadena):
    # Paso 1: Filtrar la cadena para conservar solo caracteres alfanuméricos
    # isalnum() es un método de las cadenas de texto en Python que retorna True si todos los caracteres en la cadena son alfanuméricos (es decir, letras o números), y False en caso contrario.
    cadena_filtrada = ''.join(caracter for caracter in cadena if caracter.isalnum())
    
    # Paso 2: Convertir la cadena filtrada a minúsculas
    cadena_filtrada = cadena_filtrada.lower()  # Convertir a minúsculas para tratar acentos
    
    # Paso 3: Sustituir los caracteres acentuados por sus equivalentes sin acento
    cadena_filtrada = cadena_filtrada.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    
    # Paso 4: Verificar si la cadena filtrada es igual a su imagen reflejada
    return cadena_filtrada == cadena_filtrada[::-1]

# Pedir al usuario que ingrese la frase
frase = input("Ingresa una frase para verificar si es un palíndromo: ")

# Verificar si es un palíndromo
if verificar_palindromo(frase):
    print(f'"{frase}" es un palíndromo.')
else:
    print(f'"{frase}" no es un palíndromo.')
