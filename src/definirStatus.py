from src.definirPresençaNoDF import definirPresençaNoDF
def definirStatus(primeira_metade, segunda_metade,nome,data):
    status = 'Sem registro'
    total = 0    
    if primeira_metade=="FALSE" and segunda_metade=="FALSE":#Então o aluno veio
        status = 'x'
        total = 2
    elif primeira_metade=="FALSE" and segunda_metade=="TRUE": #Veio somente entre as 18 e as 20h
        status = 'm'
        total = 1
    elif primeira_metade=="TRUE" and segunda_metade=="FALSE": #Veio somente entre as 20 e as 22h
        status = 'm' # status = '1/2 - S'
        total = 1
    elif primeira_metade=="TRUE" and segunda_metade=="TRUE": #Então ele faltou
        status = '-' #teste
        total = 0
    elif primeira_metade=="Sem registro" and segunda_metade=="Sem registro":
        status = 'Sem registro'
        total = 0
    elif primeira_metade=="Sem registro" and segunda_metade=="TRUE":
        status = '-' #Sem registro na primeira metade, porém houve na segunda metade foi registrado como falta 
        total = 0
    elif primeira_metade=="Sem registro" and segunda_metade=="FALSE":
        status = 'm' # status = 'ms' Sem registro na primeira metade, porém presente segunda metade
        total = 1
    elif primeira_metade=="TRUE" and segunda_metade=="Sem registro":
        status = '-' #Sem registro na segunda metade, porém foi registrado falta na primeira metade 
        total = 0
    elif primeira_metade=="FALSE" and segunda_metade=="Sem registro":
        status = 'm' # status = 'mp'Sem registro na segunda metade, porém foi registrado presença na primeira metade 
        total = 1
    #print(status)      
    definirPresençaNoDF(nome,status,total,data)