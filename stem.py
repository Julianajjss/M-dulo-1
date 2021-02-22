def diferenca_idade(ano_nascimentogr, ano_nascimentoju, ano_atual):
    idade_grace = 115 - ano_nascimentogr
    idade_ju = ano_atual - ano_nascimentoju

    idade_diferenca = idade_grace - idade_ju
    return idade_diferenca

resultado_diferenca = diferenca_idade (1906,1999,2021)

print(f'Diferença de idade entre você e Grace Hopper: {resultado_diferenca}')
