"""Mi primer programa Python"""

# Con esta línea se pide la frase y se guarda en una variable
frase = input("Introduce la frase que quieres comprobar\n")

# En esta línea se declara la función con la variable frase como parámetro


def esPalindromo(palindro):
    # Declaración de la variable para índice decreciente, como los índices empiezan por 0, la longitud total = longitud -1:
    palindro = frase
    indice = len(palindro)-1
    # Aqui se declara un bucle while con la longitud del índice como premisa:
    while indice >= 0:
        # Aqui se declara la variable letra que guarda la letra de la frase declarada en el indice:
        letra = palindro[indice]
        # Aqui se imprime la letra. Es solo para comprobar el funcionamiento del código:
        # print(letra)
        # En esta línea se resta 1 al índice para que itere en las letras de la frase y las muestre todas.
        indice = indice-1
    # Esta línea determina que el índice va a ser creciente, de 0 a [-1]
    indice = 0
    # Esta línea es para que en las comprobaciones no se peguen las dos frases:
    # print("\n")
    # Aquí se declara el segundo bucle while con la condición de que el índice debe ser menor que la longitud total de la frase
    while indice < len(palindro):
        # Aquí se declara la variable letra2 que guardará la salida de la iteración:
        letra2 = palindro[indice]
        # Aqui se imprime la salida. Es solo para comprobar cómo está funcionando el código hasta aquí.
        # print(letra2)
        # En la siguiente línea se añade una unidad al índice para que el bucle itere en todas las letras de la frase:
        indice = indice + 1
    # En la siguiente línea se añade el condicional if para comparar las variables que guarda las letras en los bucles anteriores:

    mensaje = "Es palíndromo" if letra == letra2 else "No es palíndromo"
    print(mensaje)


esPalindromo(frase)
