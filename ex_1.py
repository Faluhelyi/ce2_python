class exe_1:
    def media(list1: list) -> float:
        """
        Função para calcular a média de uma lista.
        """
        if len(list1) == 0:
            return None
        soma = sum(list1)
        media = soma / len(list1)
        return round(media, 4)

    def var(self, list1: list) -> float:
        if len(list1) ==0:
            return None

        media = exe_1.media(list1)

        var = sum([(i - media) ** 2 for i in list1])/ (len(list1)-1)
        return round(var, 4)
    

#################################################################################
################################### SOLUCAO #####################################
#################################################################################
obs = {'Acre': [0.71, 75.3], 'Amapá': [0.688, 75], 'Amazonas': [0.7, 73], 'Pará': [0.69, 73],\
       'Rondônia': [0.7, 72.2], 'Roraima': [0.669, 72.9], 'Tocantins': [0.731, 74.6]}

idh_2021 = []
exp_vida = []
for i in obs:
    idh_2021.append(obs[i][0])
    exp_vida.append(obs[i][1])

#########
### 1 ###
#########
resp = {'IHD médio em 2021': exe_1.media(idh_2021), 'Expectativa de vida média': exe_1.media(exp_vida)}
print(f'1. Calcule as médias do IDH e da expectativa de vida: {resp}'
    )
