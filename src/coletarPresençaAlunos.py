from src.utils import presença, prod, criador_dict, filtro
from src.alunosDict import dictId

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