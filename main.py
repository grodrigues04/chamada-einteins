import json
import pandas as pd
from src.ColetarDatas import coletarDatas
from src.coletarPresençaAlunos import coletarPresençaAlunos
from src.determinarFrequencia import determinarFrequencia

from src.utils import presença, DataFrameOfPresença, presençaPorcentagem, totalDePresenças


print('Coletando as Datas...')
coletarDatas()
print('Coletando as Presenças dos Alunos...')
coletarPresençaAlunos()
print('Determinando as Frequencias...')
determinarFrequencia()
porcentagemTotal = {key: f"{value/totalDePresenças * 100:.1f}%" for key, value in presençaPorcentagem.items()}
DataFrameOfPresença[f'Porcentagem. Total:{totalDePresenças}'] = porcentagemTotal                
presença[f'Porcentagem. Total:{totalDePresenças}'] = porcentagemTotal                

with open('./assets-generate/presença.json', 'w') as f:
    json.dump(presença, f, indent=4, default=str)

with open('./assets-generate/DataFrameOfPresença.json', 'w') as f:
    json.dump(DataFrameOfPresença, f, indent=4, default=str)


print('Arquivo "presença.json" criado com sucesso!')
df = pd.DataFrame(DataFrameOfPresença)
df.to_csv('./assets-generate/Chamada Geral.csv')
print('Planilha "Chamada Geral" com sucesso!')
