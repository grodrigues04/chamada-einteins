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

'''
    Fazer um dicionario, que as chaves são todas as datas
    e para cada data, vai entrar uma chave que o nome é o aluno

    

'''