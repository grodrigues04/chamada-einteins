import pandas as pd
from time import sleep

from alunosDict import dictId
import json
id_alunos = pd.read_csv('./assets/ID Alunos - Página1.csv')
prod = pd.read_csv('./assets/Planilha prod - Raw (3).csv')
presença = {}
presençaPorcentagem = {}
totalDeDias = ((prod.shape[0])//236) + 1

#para cada dia de aula (23 no total), vamos percorrer 236 linhas
totalDePresenças = (((prod.shape[0])//236)*4)-20
filtro = {
    "TRUE":"TRUE",
    "FALSE":"FALSE",
    "VERDADEIRO":"TRUE",
    "FALSO":"FALSE"
}


criador_dict = {
    "TRUE":"primeira_metade",
    "FALSE":"segunda_metade"
}
def coletarDatas():
    for dataLinha in range(1,prod.shape[0],50):
        data = prod.iloc[dataLinha,3]
        dia = data[8:10]
        mes = data[5:7:1]
        # BUG: dia sempre estara em presença
        # porque o que é adicionado é o dia/mes
        # no final da certo mas nao é correto
        # corr -> if f'{dia}/{mes}' not in presença:
        if dia not in presença:
            # print(dataLinha, f'{dia}/{mes}')
            presença[f'{dia}/{mes}'] = {}
    # print(presença)
coletarDatas()
diasTestador = []
presençaDf = presença.copy()
def coletarPresençaAlunos():
    for linha in range(1,prod.shape[0]):
        #print(linha)
        criado_em = prod.iloc[linha,3]
        dia = criado_em[8:10]
        mes = criado_em[5:7:1]
        #print(dia)
        alunoId = prod.iloc[linha,1]
        alunoNome = dictId[alunoId]
        dia_atual = presença[f'{dia}/{mes}']
        #print(filtro[prod.iloc[linha, 4]])
        #print(f'{dia}/{mes}')
        diasTestador.append(f'{dia}/{mes}')
        if alunoNome not in presença[f'{dia}/{mes}']: #Então adiciona o aluno
            dia_atual[alunoNome] = {} #criando o dic do aluno
            alunoDict = dia_atual[alunoNome]
            alunoDict['id'] = alunoId
        else:
            alunoDict = dia_atual[alunoNome] #pegando apenas o dict do aluno
            valorAtualPrimeira_metade = filtro[prod.iloc[linha,4]]
            chave = criador_dict[valorAtualPrimeira_metade]
            alunoDict[chave] = filtro[prod.iloc[linha,2]]
coletarPresençaAlunos()

    
# def determinarFrequencia():
#     for item in presença: #chave data
#         print(item)
#         alunos = presença[item]
#         for aluno in alunos:
#             if aluno['primeira_metade_T_falta'] == "TRUE":
#                 #wadasd


with open('presença.json', 'w') as f:
    json.dump(presença, f, indent=4, default=str)

# Imprimir o dicionário organizado
# print(presença_json)


print('Arquivo JSON criado com sucesso!')


#print(presença)

















df = pd.DataFrame(presença)
df.to_csv('Chamada Geral ultima.csv')
print('Planilha criada com sucesso!')
