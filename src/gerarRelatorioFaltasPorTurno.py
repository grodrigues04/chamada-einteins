from collections import defaultdict
import pandas as pd
from datetime import datetime
from utils import prod


def gerarRelatorioFaltasPorTurno():
    faltas_por_mes_1turno = defaultdict(int)
    faltas_por_mes_2turno = defaultdict(int)

    meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ]

    for mes in meses:
        for index, row in prod:
            if((prod[index, 2]== "TRUE" or prod[index, 2]== "VERDADEIRO") and prod.iloc[index,3].month_name == meses[mes] and (prod[index, 4]=="VERDADEIRO" or prod[index, 4]=="TRUE")):
                mes = datetime.strptime(row[3], '%Y-%m-%d').strftime('%B')
                # Incrementar o contador para o mês correspondente
                faltas_por_mes_1turno[mes] += 1
            elif((prod[index, 2]== "FALSE" or prod[index, 2]== "FALSO") and prod.iloc[index,3].month_name == meses[mes] and (prod[index, 4]=="FALSO" or prod[index, 4]=="FALSE")):    
                mes = datetime.strptime(row[3], '%Y-%m-%d').strftime('%B')
                # Incrementar o contador para o mês correspondente
                faltas_por_mes_2turno[mes] += 1


    data = {
        'Mês': [],
        'Primeiro turno': [],
        'Segundo turno': []
    }

    for mes in meses:
        data['Mês'].append(mes)
        data['Primeiro turno'].append(faltas_por_mes_1turno[mes])
        data['Segundo turno'].append(faltas_por_mes_2turno[mes])

    df = pd.DataFrame(data)

    # Adiciona a coluna "Turno"
    df_melted = df.melt(id_vars=['Mês'], var_name='Turno', value_name='Faltas')

    # Salva o DataFrame em um arquivo CSV
    df_melted.to_csv('faltas_por_turno.csv', index=False)

    return df_melted
