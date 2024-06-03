import pandas as pd
from alunosDict import dictId
import json

id_alunos = pd.read_csv('./assets/ID Alunos - Página1.csv')
prod = pd.read_csv('./assets/Planilha prod - Raw (3).csv')
debuger = pd.read_csv('test_df.csv')
presença = {}
DataFrameOfPresença = {}
presençaPorcentagem = {}
totalDeDias = ((prod.shape[0])//236) + 1

#para cada dia de aula (23 no total), vamos percorrer 236 linhas
totalDePresenças = (((prod.shape[0])//236)*2)-8
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
            DataFrameOfPresença[f'{dia}/{mes}'] = {}


coletarDatas()



def coletarPresençaAlunos():
    for linha in range(1,prod.shape[0]):
        criado_em = prod.iloc[linha,3]
        dia = criado_em[8:10]
        mes = criado_em[5:7:1]
        alunoId = str(prod.iloc[linha,1])
        alunoNome = dictId[alunoId]
        dia_atual = presença[f'{dia}/{mes}']

        valorAtualPrimeira_metade = filtro[prod.iloc[linha,4]]
        chave = criador_dict[valorAtualPrimeira_metade]

        if alunoNome not in presença[f'{dia}/{mes}']: #Então adiciona o aluno
            dia_atual[alunoNome] = {} #criando o dic do aluno
            alunoDict = dia_atual[alunoNome]
            alunoDict['id'] = alunoId
            valorAtualPrimeira_metade = filtro[prod.iloc[linha,4]]
            chave = criador_dict[valorAtualPrimeira_metade]
            alunoDict[chave] = filtro[prod.iloc[linha,2]]
        else:
            alunoDict = dia_atual[alunoNome] #pegando apenas o dict do aluno
            valorAtualPrimeira_metade = filtro[prod.iloc[linha,4]]
            chave = criador_dict[valorAtualPrimeira_metade]
            alunoDict[chave] = filtro[prod.iloc[linha,2]]
coletarPresençaAlunos()

def definirStatus(primeira_metade, segunda_metade,nome,data):
    if primeira_metade=="FALSE" and segunda_metade=="FALSE":#Então ele veio
        status = 'presente'
        total = 2
    elif primeira_metade=="FALSE" and segunda_metade=="TRUE": #Veio somente entre as 18 e as 20h
        status = '1/2 - P'
        total = 1
    elif primeira_metade=="TRUE" and segunda_metade=="FALSE": #Veio somente entre as 20 e as 22h
        status = '1/2 - S'
        total = 1
    elif primeira_metade=="TRUE" and segunda_metade=="TRUE": #Então ele faltou
        status = 'Ausente'
        total = 0
    elif primeira_metade=="Sem registro" and segunda_metade=="Sem registro":
        status = 'Sem registro'
        total = 0
    elif primeira_metade=="Sem registro" and segunda_metade=="TRUE":
        status = '0/2 - SRFS' #Sem registro na primeira metade, porém houve na segunda metade foi registrado como falta 
        total = 0
    elif primeira_metade=="Sem registro" and segunda_metade=="FALSE":
        status = '1/2 - SRPS' #Sem registro na primeira metade, porém presenta segunda metade
        total = 1
    elif primeira_metade=="TRUE" and segunda_metade=="Sem registro":
        status = '0/2 - SRFP' #Sem registro na segunda metade, porém foi registrado falta na primeira metade 
        total = 0
    elif primeira_metade=="FALSE" and segunda_metade=="Sem registro":
        status = '1/2 - SRFP' #Sem registro na segunda metade, porém foi registrado presença na primeira metade 
        total = 1
    #print(status)      
    definirPresençaNoDF(nome,status,total,data)

def definirPresençaNoDF(nome,status,total,data):
    DataFrameOfPresença[data][nome] = status
    #print(presençaPorcentagem)
    if nome not in presençaPorcentagem:
        presençaPorcentagem[nome] = total
    else:
        presençaPorcentagem[nome] += total
def determinarFrequencia():
    for item in presença: #chave data
        data = item
        alunos = presença[item]
        for aluno in alunos:
            nome = aluno
            alunoDictInfo = presença[data][aluno]
            #print(alunoDictInfo)
            presençaS = 'Sem registro'
            presençaP = 'Sem registro'
            if 'primeira_metade' in alunoDictInfo:
                #print('entrei')
                presençaP = alunoDictInfo['primeira_metade']
                if 'segunda_metade' in alunoDictInfo: #se não existir, ele não entra no IF, e a presença na segunda metade fica "sem registro"
                    presençaS = alunoDictInfo['segunda_metade']
                    definirStatus(presençaP,presençaS, nome,data)
                    continue #vai pro proximo estudante
            else:
                if 'segunda_metade' in alunoDictInfo:
                    presençaS = alunoDictInfo['segunda_metade']
                    definirStatus(presençaP,presençaS, nome,data)
                    continue #vai pro proximo estudante
                definirStatus(presençaP,presençaS, nome,data)
                continue #vai pro proximo estudante

determinarFrequencia()
porcentagemTotal = {key: f"{value/totalDePresenças * 100:.1f}%" for key, value in presençaPorcentagem.items()}
print(porcentagemTotal)
DataFrameOfPresença[f'Porcentagem. Total:{totalDePresenças}'] = porcentagemTotal                
presença[f'Porcentagem. Total:{totalDePresenças}'] = porcentagemTotal                

with open('presença.json', 'w') as f:
    json.dump(presença, f, indent=4, default=str)

with open('DataFrameOfPresença.json', 'w') as f:
    json.dump(DataFrameOfPresença, f, indent=4, default=str)

# Imprimir o dicionário organizado
# print(presença_json)


print('Arquivo "presença.json" criado com sucesso!')
print(presençaPorcentagem)
df = pd.DataFrame(DataFrameOfPresença)
df.to_csv('Chamada Geral sera que vai.csv')
print('Planilha "Chamada Geral sera que vai" com sucesso!')
