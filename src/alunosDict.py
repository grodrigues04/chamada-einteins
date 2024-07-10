import pandas as pd
id_alunos = pd.read_csv('./assets/ID Alunos - Página1.csv')

linhas = id_alunos.shape[0]

dictId = {}

for l in range(linhas):
    dictId[str(id_alunos.iloc[l,0])] = id_alunos.iloc[l,1]

