import pandas as pd
from time import sleep
palavra = "gustavo"
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
def coletarDatas():
    for dataLinha in range(1,prod.shape[0],50):
        data = prod.iloc[dataLinha,3]
        dia = data[8:10]
        mes = data[5:7:1]
        if dia not in presença:
            presença[f'{dia}/{mes}'] = {}
    #print(presença)
coletarDatas()
diasTestador = []
presençaDf = presença.copy()
def coletarPresençaAlunos():
    for linha in range(1,prod.shape[0]):
        print(linha)
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
            alunoDict = dia_atual[alunoNome] #pegando apenas o dict do aluno
            alunoDict['id'] = alunoId
            if filtro[prod.iloc[linha,4]] == "TRUE":
                alunoDict['primeira_metade'] = f'{filtro[prod.iloc[linha,2]]}'
            else:
                alunoDict['segunda_metade'] = f'{filtro[prod.iloc[linha,2]]} do primeiro if'
        else:
            alunoDict = dia_atual[alunoNome] #pegando apenas o dict do aluno
            print(linha)
            print('essa condição é: ', 'primeira_metade' in alunoDict)
            print(alunoDict)
            #sleep(0.5)
            if 'primeira_metade' in alunoDict:
                alunoDict['segunda_metade'] = f'{filtro[prod.iloc[linha,2]]}'
            else:
                alunoDict['primeira_metade'] = f'{filtro[prod.iloc[linha,2]]} primeira metade do segundo'
            print('novo:')
            print(alunoDict)
coletarPresençaAlunos()

    
# def determinarFrequencia():
#     for item in presença: #chave data
#         print(item)
#         alunos = presença[item]
#         for aluno in alunos:
#             if aluno['primeira_metade_T_falta'] == "TRUE":
#                 #wadasd





with open('presençaDOIS.json', 'w') as json_file:
    json.dump(presença, json_file, indent=4, ensure_ascii=False)

with open('aaaaaa.json', 'w') as json_file:
    json.dump(diasTestador, json_file, indent=4, ensure_ascii=False)

print('Arquivo JSON criado com sucesso!')


#print(presença)

















df = pd.DataFrame(presença)
df.to_csv('Chamada Geral ultima.csv')
print('Planilha criada com sucesso!')
