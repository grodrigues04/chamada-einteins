import pandas as pd
palavra = "gustavo"
from alunosDict import dictId
id_alunos = pd.read_csv('./assets/ID Alunos - Página1.csv')
prod = pd.read_csv('./assets/Planilha prod - Raw (3).csv')
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
for c in range(totalDeDias):
    dia_coleta_prod = prod.iloc[linhaDatas,3]
    diaDict = f'{dia_coleta_prod[8:10]}/{dia_coleta_prod[5:7]}'
    presença[diaDict] = {}
    for c in range(linhaInico,linhaFinal):
        PrimeiroBlocoFalta = prod.iloc[c,2]
        PrimeiroBloco = prod.iloc[c,4]
        SegundoBlocoFalta = prod.iloc[c+180,2]
        SegundoBloco = prod.iloc[c+180,4]
        aluno = dictId[prod.iloc[c,1]]
        #FILTRANDO
        PrimeiroBlocoFalta = filtro[PrimeiroBlocoFalta]
        SegundoBlocoFalta = filtro[SegundoBlocoFalta]
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
        presença[diaDict][aluno] = status
        if aluno not in presençaPorcentagem:
            presençaPorcentagem[aluno] = total
        else:
            pontos = presençaPorcentagem[aluno] + total
            presençaPorcentagem[aluno] = pontos
        #print(presençaPorcentagem)

    linhaInico = linhaFinal
    linhaFinal = linhaFinal + 119
    linhaDatas += 236

porcentagem = {key: f"{value/totalDePresenças * 100:.1f}%" for key, value in presençaPorcentagem.items()}

presença['Porcentagem'] = porcentagem
presença['Total: 68'] = presençaPorcentagem
df = pd.DataFrame(presença)
#df.to_csv('Chamada Geral.csv')
print('Planilha criada com sucesso!')


a = presença['19/04']
for aluno in a:
    print(aluno,':',a[aluno])