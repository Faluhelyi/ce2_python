class lista1_values:
    """
    Recebe como entrada valores em formato de dicionário.
    """
    def __init__(self, obs):
        self.obs = obs


class lista1:
    """
    classe para solucionar a lista 1
    """
    def __init__(self):
        self.obs = {}

    def media(self):
        media = {}
        for k in self.obs:
            media[k] = sum(self.obs[k])/len(self.obs[k])
            media[k] = round(media[k], 4)

        return media
    
    def sort(self, ascending = True):
        """
        Recebe um dicionário. Para cada chave do dicionário,\n
        a funcao vai ordenar as valores da chave correspondente
        """
        sort = {}
        for k in self.obs:
            if ascending == True:
                sort[k] = self.obs[k]
                n = len(sort[k])
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if sort[k][j]>sort[k][j+1]:
                            sort[k][j], sort[k][j+1] = sort[k][j+1], sort[k][j]

            else:
                sort[k] = self.obs[k]
                n = len(sort[k])
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if sort[k][j]<sort[k][j+1]:
                            sort[k][j], sort[k][j+1] = sort[k][j+1], sort[k][j]

        return sort
    
    def mediana(self):
        self.obs = lista1.sort(self)
        mediana = {}
        for k in self.obs:
            n = len(self.obs[k])
            pos = int(n/2)
            if n%2 == 0:
                mediana[k] = (self.obs[k][pos-1] + self.obs[k][pos])/2
            else:
                mediana[k] = self.obs[k][pos]

        return mediana
    
    def moda(self):
        self.obs = lista1.sort(self, ascending= False)
        moda = {}
        for k in self.obs:
            moda[k] = max(self.obs[k], key=self.obs[k].count)

            if self.obs[k].count(moda[k]) == 1:
                moda[k] = 'Não tem moda'

        return moda




obs = {'Acre': [0.71, 75.3], 'Amapá': [0.688, 75], 'Amazonas': [0.7, 73], 'Pará': [0.69, 73],\
       'Rondônia': [0.7, 72.2], 'Roraima': [0.669, 72.9], 'Tocantins': [0.731, 74.6]}

#################################################################################
################################### SOLUCAO #####################################
#################################################################################
idh_2021 = []
exp_vida = []

for i in obs:
    idh_2021.append(obs[i][0])
    exp_vida.append(obs[i][1])

#########
### 1 ###
#########
obs1 = lista1_values({'IDH 2021 médio': idh_2021, 'Expectativa de vida média': exp_vida})
print(f'1. Calcule as médias do IDH e da expectativa de vida: {lista1.media(obs1)}'
    )

#########
### 2 ###
#########
obs2 = lista1_values({'IDH 2021 mediano': idh_2021, 'Expectativa de vida mediana': exp_vida})
print(f'2. Calcule as medianas do IDH e da expectativa de vida: {lista1.mediana(obs2)}'
)

#########
### 3 ###
#########
obs3 = lista1_values({'moda para IDH 2021': [1,2,3,4,4,4,5,6,6, 6], 'moda para Expectativa de vida': exp_vida})
print(f'3. Existe alguma moda no IDH e na expectativa de vida? Caso afirmativo, qual(is) a(s) moda(s): {lista1.moda(obs3)}'
)

print(lista1.sort(obs3, ascending=False))
