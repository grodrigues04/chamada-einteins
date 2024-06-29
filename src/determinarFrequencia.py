from src.utils import presença
from src.definirStatus import definirStatus

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