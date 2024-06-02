import pandas as pd
import json
palavra = "gustavo"
from alunosDict import dictId
id_alunos = pd.read_csv('./assets/ID Alunos - Página1.csv')
prod = pd.read_csv('./assets/Planilha prod - Raw (3).csv')
#print(dictId)
presença = {}
presençaPorcentagem = {}
horario = {
    17:"",
    18:"",
    19:"",
    20:"",
    21:"",
    22:""
}
totalDeDias = ((prod.shape[0])//236) + 1
#print(totalDeDias)
#para cada dia de aula (23 no total), vamos percorrer 236 linhas
linhaInico = 1
linhaFinal = 119
linhaDatas = 1

totalDePresenças = (((prod.shape[0])//236)*4)-20
filtro = {
    "TRUE":"TRUE",
    "FALSE":"FALSE",
    "VERDADEIRO":"TRUE",
    "FALSO":"FALSE"
}
testador = ''
data = {}
for c in range(totalDeDias-2):
    dia_coleta_prod = prod.iloc[linhaDatas,3]
    diaDict = f'{dia_coleta_prod[8:10]}/{dia_coleta_prod[5:7]}'
    #print(diaDict)
    presença[diaDict] = {}
    data[diaDict] = {}
    comparador = "primeira_metade_true"
    for linhaDf in range(linhaInico,linhaFinal):
        #print(linhaDf)
        PrimeiroBlocoFalta = filtro[prod.iloc[linhaDf,2]]
        primeira_metade_boleano = filtro[prod.iloc[linhaDf,4]]    
        aluno = dictId[prod.iloc[linhaDf,1]]
        idAlunoPrimeiraMetade = prod.iloc[linhaDf,1]
        controlador = True
        if primeira_metade_boleano != "TRUE":
            primeiro_bloco_cima = linhaInico + 1
            primeiro_bloco_baixo = linhaInico -1
            #print('entri aqui')
            while controlador:
                primeiro_bloco_baixoTeste = filtro[prod.iloc[primeiro_bloco_baixo,2]]
                primeiro_bloco_cimaTeste = filtro[prod.iloc[primeiro_bloco_cima,2]]
                #print('PROCURANDO:',{prod.iloc[primeiro_bloco_cima,1]})
                #print('BC ->',{primeiro_bloco_cimaTeste},':',prod.iloc[primeiro_bloco_cima,1], 'BB ->',{primeiro_bloco_baixoTeste},":",prod.iloc[primeiro_bloco_baixo,1])
                if primeiro_bloco_cimaTeste=="TRUE" and prod.iloc[primeiro_bloco_cima,1]==idAlunoPrimeiraMetade:
                    PrimeiroBlocoFalta = filtro[prod.iloc[primeiro_bloco_cima,2]]
                    break
                elif primeiro_bloco_baixoTeste=="TRUE" and prod.iloc[primeiro_bloco_baixo,1]==idAlunoPrimeiraMetade:
                    PrimeiroBlocoFalta = filtro[prod.iloc[primeiro_bloco_baixo,2]]
                    break
                else:
                    primeiro_bloco_cima+=1
                    primeiro_bloco_baixo-=1
        print('Primeiro bloco Falta definido!', c)
        if aluno not in data[diaDict]:
            data[diaDict][aluno] = {
                "linhaP":linhaDf,
                "primeiro_bloco_falta":PrimeiroBlocoFalta
            }
        linhaProcuradora = linhaDf + 1

        #print(data)
        while comparador== "primeira_metade_true":
            #print(linhaProcuradora)
            valor_coluna_PrimeiraMetade = filtro[(prod.iloc[linhaProcuradora,4])]
            #print(valor_coluna_PrimeiraMetade, "TRUE")
            if valor_coluna_PrimeiraMetade == "TRUE":
                linhaProcuradora+=1
                #print('somei')
            else:
                idAlunoSegundaMetade = prod.iloc[linhaProcuradora,1]
                if idAlunoPrimeiraMetade==idAlunoSegundaMetade:
                    SegundoBlocoFalta = filtro[prod.iloc[linhaProcuradora,2]]
                    data[diaDict][aluno]["linhaS"] = linhaProcuradora
                    data[diaDict][aluno]["segundo_bloco_falta"] = SegundoBlocoFalta
                    #print('TUDO CERTO')
                    break

                else:
                    #print('Entrei na primeira metade false, mas o id ta errado')
                    linhaProcuradora+=1
        if PrimeiroBlocoFalta== "TRUE" and SegundoBlocoFalta=="TRUE":
            status = 'Ausente'
            total = 0
        elif PrimeiroBlocoFalta=="FALSE" and SegundoBlocoFalta=="FALSE":
            status = '4/4'
            total = 4
        elif PrimeiroBlocoFalta=="FALSE" and SegundoBlocoFalta=="TRUE":
            status = '2/4 - P'
            total = 2
        elif PrimeiroBlocoFalta=="TRUE" and SegundoBlocoFalta=="FALSE":
            status = '2/4 - S'
            total = 2
        #print('STATUS:','P',PrimeiroBlocoFalta,'S',SegundoBlocoFalta)
        presença[diaDict][aluno] = status
        if aluno not in presençaPorcentagem:
            presençaPorcentagem[aluno] = total
        else:
            pontos = presençaPorcentagem[aluno] + total
            presençaPorcentagem[aluno] = pontos
        #print(presençaPorcentagem)

    linhaInico = linhaFinal + 118
    linhaFinal = linhaInico + 118
    linhaDatas += 236

porcentagem = {key: f"{value/totalDePresenças * 100:.1f}%" for key, value in presençaPorcentagem.items()}
for item in data:
    print(item,":",data[item])
    print()
presença['Porcentagem'] = porcentagem
presença[f'Total: {totalDePresenças}'] = presençaPorcentagem
df = pd.DataFrame(presença)
df.to_csv('Chamada Geral.csv')
print('Planilha criada com sucesso!')
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)
