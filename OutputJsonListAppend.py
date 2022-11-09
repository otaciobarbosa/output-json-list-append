dicionario ={
    'pessoa_1':{
        'nome':'Peterson',
        'sobrenome':'Almeida'
    }, 
    'pessoa_2':{
        'nome':'Maria',
        'sobrenome':'Silva'
    },
    'pessoa_3':{
        'nome':'Jose',
        'sobrenome':'Santos'
    }
}

nomecompleto = []
i = 0
for i in dicionario:
 nome = dicionario[i]['nome']+' '+ dicionario[i]['sobrenome']
 nomecompleto.append(nome)

 print(nomecompleto)