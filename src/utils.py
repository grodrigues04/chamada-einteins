import pandas as pd
presença = {}
DataFrameOfPresença = {}
presençaPorcentagem = {}
#para cada dia de aula (23 no total), vamos percorrer 236 linhas
id_alunos = pd.read_csv('./assets/ID Alunos - Página1.csv')
prod = pd.read_csv('./assets/planilha_prod.csv')

totalDePresenças = (((prod.shape[0])//236)*2)-31 #16 - desconsidera dias que NENHUM estudante foi coletado. 15 -desconsidera as férias (16+15=31)
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

meses = {
    "01":"Janeiro",
    "02":"Fevereiro",
    "03":"Março",
    "04":"Abril",
    "05":"Maio",
    "06":"Junho",
    "07":"Julho",
    "08":"Agosto",
    "09":"Setembro",
    "10":"Outubro",
    "11":"Novembro",
    "12":"Dezembro"
}

totaisDeDiaPorMes = {
    'Janeiro': 0,
    'Fevereiro': 0,
    'Março': 0,
    'Abril': -5, #as semaninhas são desconsideradas
    'Maio': -3,
    'Junho': 0,
    'Julho': -15,
    'Agosto': 0,
    'Setembro': 0,
    'Outubro': 0,
    'Novembro': 0,
    'Dezembro': 0
}

valorPresença = {
    "x": 2,
    "m": 1,
    "Sem registro": 0,
    "-":0,
}

presençaMensal = {}

