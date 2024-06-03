import pandas as pd

# para carregar o dataframe limpo
# le e limpa o dataframe
def csv_load_clean_data(path = './assets/Planilha prod - Raw (3).csv'):
    ## "Ajeita" o dataframe e salva um df de testes
    data = pd.read_csv(path)
    # seta as colunas como a primeira linha
    data.columns = data.iloc[0]
    # exclui a primeira linha
    data = data.drop(0)

    # converte as datas para datetime
    # isso é preciso porque depois podemos fazer comparações com datas
    data['criado_em'] = pd.to_datetime(data['criado_em'])

    # retorna o dataframe
    return data



data = csv_load_clean_data()
# deleta a maioria das linhas so para testar
data = data[
    (
        (data['aluno_id'] == "120") | ## ou
        (data['aluno_id'] == "121") |
        (data['aluno_id'] == "168") 
    )
    & ## e
    (data['criado_em'] < pd.to_datetime('2024-05-07'))
    ]
# salva o dataframe
data.to_csv("test_df.csv", index=False)



