class Palabra():

    def __init__(self, cadena):
        self.cadena=cadena

    def getCadena(self):
        return self.cadena

    def invertirCadena(self):
        return(self.cadena[::-1])

    def esPalindromo(self):
        if self.getCadena() == self.invertirCadena():
            print("Es palindromo")
        else:
            print("No es palindromo")

c = Palabra("dabale arroz a la zorra el abad")
c.esPalindromo()