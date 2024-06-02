import pandas as pd
presença ={
    "27/05":{ 
        "gustavo":'Atrasado',
        "Pedro":'Atrasado',
        "Julia":'Presente'

    },
    "28/05":{ 
        "gustavo":'Presente',
        "Pedro":'Presente',
        "Julia":'Faltou'

    },
    "29/05":{ 
        "gustavo":'Atrasado',
        "Pedro":'Presente',
        "Julia":'Atrasado'

    },
    "30/05":{ 
        "gustavo":'Atrasado',
        "Pedro":'Atrasado',
        "Julia":'Presente'

    },
    "31/05":{ 
        "gustavo":'Atrasado',
        "Pedro":'Atrasado',
        "Julia":'Presente'

    }
}




df = pd.DataFrame(presença)
df.to_csv('testePresençaUM.csv')


data = {} 
atual = {
    "gustavo":{
        "linha": "123",
        "primeira_metade_false":"120",
        "primeira_metade_true":"120",
    }
}

data["19/04"] = atual
print(data)