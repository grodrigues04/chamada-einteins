from src.utils import presençaMensal, totaisDeDiaPorMes,valorPresença, meses
import json
#logica do script: conta quantas ocorrencias cada estudante tem de "m" e "x" no json "jsonParaPresença"
def readJson():
    json_path = './assetsGenerate/jsonParaPresencaMensal.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    return dados
def calcularPorcentagem():
    for mes in presençaMensal:
        alunosMes = presençaMensal[mes]
        for aluno in alunosMes:
            pontos = alunosMes[aluno]
            total_de_dias = totaisDeDiaPorMes[mes]
            porcentagem = f'{(pontos/(total_de_dias*2))*100:.1f}'
            alunosMes[aluno] = porcentagem
    
            
            
def adiconarDiasTotais(mouth):
    totaisDeDiaPorMes[mouth]+=1

        

def calculo(jsonObject,dia, dictData):
    data = jsonObject[dia]
    for item in data:
        aluno = item
        if aluno not in dictData:
            valor = valorPresença[data[item]]
            dictData[aluno] = valor
        else:
            dictData[aluno] = dictData[aluno] + valorPresença[data[item]]
    
    # for item in dictData:
    #     print(item, dictData[item])
    # print()

def definirNumeroPresençaMensal():
    jsonObject = readJson()
    for data in jsonObject:
        mouth = meses[str(data)[3::]]
        #print(mouth)
        adiconarDiasTotais(mouth)
        if mouth not in presençaMensal:
            presençaMensal[mouth] = {}
        calculo(jsonObject,data, presençaMensal[mouth])



def mensal():
    definirNumeroPresençaMensal()
    calcularPorcentagem()
    
if __name__ == "__main__":
    mensal()