from src.utils import presença, DataFrameOfPresença, prod
def coletarDatas():
    for dataLinha in range(1,prod.shape[0],50):
        data = prod.iloc[dataLinha,3]
        dia = data[8:10]
        mes = data[5:7:1]
        if dia not in presença:
            presença[f'{dia}/{mes}'] = {}
            DataFrameOfPresença[f'{dia}/{mes}'] = {}
   # print(presença)
