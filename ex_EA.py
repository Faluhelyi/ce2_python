class exe_EA:
    def media(list1: list) -> float:
        """
        Função para calcular a média de uma lista.
        """
        if len(list1) == 0:
            return None
        soma = sum(list1)
        media = soma / len(list1)
        return round(media, 4)

    def var(list1: list) -> float:
        if len(list1) < 2:
            return None

        media = exe_EA.media(list1)

        var = sum([(i - media) ** 2 for i in list1])/ (len(list1)-1)
        return round(var, 4)
    
    def sd(list1: list) -> float:
        try:
            sd = round(exe_EA.var(list1)**(0.5), 4)
        except:
            sd = None
        return sd
    
    def cov(list1: list, list2: list) -> float:
        if (len(list1) != len(list2)) | (len(list1) < 2) | (len(list2) < 2):
            return None
        else:
            media1 = exe_EA.media(list1)
            media2 = exe_EA.media(list2)
            cov = (1/(len(list1)-1))*sum([(i-media1)*(j - media2) for i, j in zip(list1, list2)])
            return round(cov, 4)
        
    def corr(list1: list, list2: list) -> float:
        if (len(list1) != len(list2)) | (len(list1) < 2) | (len(list2) < 2):
            return None
        else:
            media1 = exe_EA.media(list1)
            media2 = exe_EA.media(list2)
            numerador = sum([(i-media1)*(j-media2) for i,j in zip(list1, list2)])
            denominador = (sum([(i-media1)**2 for i in list1])**(1/2)) * (sum([(i-media2)**2 for i in list2])**(1/2))
            corr = numerador/denominador
            return round(corr, 4)
        
    def sort(list1: list, ascending: bool = True) -> list:
        """
        Recebe um dicionário. Para cada chave do dicionário,\n
        a funcao vai ordenar as valores da chave correspondente
        """
        if ascending == True:
            n = len(list1)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if list1[j]>list1[j+1]:
                        list1[j], list1[j+1] = list1[j+1], list1[j]

        else:
            n = len(list1)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if list1[j]<list1[j+1]:
                        list1[j], list1[j+1] = list1[j+1], list1[j]

        return list1
    
    def mediana(list1: list) -> float:
        list1 = exe_EA.sort(list1)
        n = len(list1)
        pos = int(n/2)
        if n%2 == 0:
            mediana = (list1[pos-1] + list1[pos])/2
        else:
            mediana = list1[pos]
        return mediana
    
    def moda(list1: list) -> float:
        list1 = exe_EA.sort(list1, ascending= False)
        moda = max(list1, key=list1.count)

        if list1.count(moda) == 1:
            moda = 'Não tem moda'

        return moda

    

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
resp1 = {'IHD médio em 2021': exe_EA.media(idh_2021), 'Expectativa de vida média': exe_EA.media(exp_vida)}
print(f'1. Calcule as médias do IDH e da expectativa de vida:\n {resp1}'
    )

#########
### 2 ###
#########
resp2 = {'IHD mediano em 2021': exe_EA.mediana(idh_2021), 'Expectativa de vida mediana': exe_EA.mediana(exp_vida)}
print(f'2. Calcule as medianas do IDH e da expectativa de vida:\n {resp2}'
    )


#########
### 3 ###
#########
resp3 = {'moda para o IHD em 2021': exe_EA.moda(idh_2021), 'moda para a Expectativa de vida': exe_EA.moda(exp_vida)}
print(f'3. Existe alguma moda no IDH e na expectativa de vida? Caso afirmativo, qual(is) a(s) moda(s):\n {resp3}'
    )


#########
### 5 ###
#########
resp5 = {'var(IDH)': exe_EA.var(idh_2021), 'sd(IDH)': exe_EA.sd(idh_2021),\
         'var(exp.vida)': exe_EA.var(exp_vida), 'sd(exp.vida)': exe_EA.sd(exp_vida)}
print(f'5. Calcule a variância e o desvio padrão do IDH e da expectativa de vida:\n {resp5}'
    )

#########
### 6 ###
#########
resp6 = {'cov(IDH, exp.vida)': exe_EA.cov(idh_2021, exp_vida), 'corr(IDH, exp.vida)': exe_EA.corr(idh_2021, exp_vida)}
print(f'6. Calcule a covariância e a correlação (use elementos calculados anteriormente) entre o IDH e a expectativa de vida:\n {resp6}'
    )
