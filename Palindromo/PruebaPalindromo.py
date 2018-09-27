def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return (invertida)

def es_palindromo (cadena):
    palabra_invertida = inversa (cadena)
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[i] == cadena[i]:
            cont += 1
        else:
            print ("No es palindromo")
            break

    if cont == len(cadena):
        print ("Es palindromo")
es_palindromo("radar")