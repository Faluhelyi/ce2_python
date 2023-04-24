class lista1_values:
    def __init__(self, obs):
        self.obs = obs


class lista1:
    def __init__(self):
        self.obs = {}

    def media(self):
        media = {}
        for k in self.obs:
            media[k] = sum(self.obs[k])/len(self.obs[k])

        return media
    
obs = {'Acre': [0.71, 75.3], 'Amapá': [0.688, 75], 'Amazonas': [0.7, 73], 'Pará': [0.69, 73], 'Rondônia': [0.7, 72.2], 'Roraima': [0.669, 72.9],\
                     'Tocantins': [0.731, 74.6]}

values = lista1_values(obs)
print(lista1.media(values))

