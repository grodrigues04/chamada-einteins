import pandas as pd
presença = {}
DataFrameOfPresença = {}
presençaPorcentagem = {}
#para cada dia de aula (23 no total), vamos percorrer 236 linhas
id_alunos = pd.read_csv('./assets/ID Alunos - Página1.csv')
prod = pd.read_csv('./assets/Planilha prod - Raw (3).csv')

totalDePresenças = (((prod.shape[0])//236)*2)-8
totalDeDias = ((prod.shape[0])//236) + 1

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
