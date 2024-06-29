from src.utils import DataFrameOfPresença, presençaPorcentagem
def definirPresençaNoDF(nome,status,total,data):
    DataFrameOfPresença[data][nome] = status
    #print(presençaPorcentagem)
    if nome not in presençaPorcentagem:
        presençaPorcentagem[nome] = total
    else:
        presençaPorcentagem[nome] += total