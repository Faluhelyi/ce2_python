class Estatistica:
    def __init__(self, lista1, lista2=None):
        self.lista1 = lista1
        self.lista2 = lista2

    def calcular_media(self, lista):
        """
        Função para calcular a média de uma lista.
        """
        if len(lista) == 0:
            return None
        soma = sum(lista)
        media = soma / len(lista)
        return media

    def calcular_variancia(self, lista):
        """
        Função para calcular a variância de uma lista.
        """
        media = self.calcular_media(lista)
        if media is None:
            return None
        soma = sum([(x - media) ** 2 for x in lista])
        variancia = soma / len(lista)
        return variancia

    def calcular_covariancia(self):
        """
        Função para calcular a covariância entre duas listas.
        """
        if self.lista2 is None:
            raise ValueError("A segunda lista não foi fornecida.")
        if len(self.lista1) != len(self.lista2):
            raise ValueError("As listas têm tamanhos diferentes.")

        media1 = self.calcular_media(self.lista1)
        media2 = self.calcular_media(self.lista2)

        soma = sum([(x1 - media1) * (x2 - media2) for x1, x2 in zip(self.lista1, self.lista2)])
        covariancia = soma / len(self.lista1)

        return covariancia
    

# Exemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]

estatistica = Estatistica(lista1, lista2)
media1 = estatistica.calcular_media(lista1)
variancia1 = estatistica.calcular_variancia(lista1)
covariancia = estatistica.calcular_covariancia()

print("Média da lista1:", media1)
print("Variância da lista1:", variancia1)
print("Covariância entre lista1 e lista2:", covariancia)