def ingredientes_lasanha():
    print('1 massa de lasanha (pronta)')
    print('500g de presunto')
    print('500g de queijo mussarela')
    print('500g de carne moida')
    print('1 pacote de massa de tomate')
    print('Sal a gosto')
    print('Orégano a gosto')

def fogao():
    print('1- Separe uma panela com 250 ml de água para cozinhar a massa por 10 minutos')
    print ('2- Em uma panela, coloque o molho junto com a carne moida e deixe cozinhar')

def montagem_forma():
    print('3 -Comece montando com uma camada de molho, a massa da lasanha, presunto e queijo. ')
    print('4 Faça esse processo até terminar os ingredientes.')

def forno():
    print('5- Pre aqueça o forno a 180º graus')
    print('6- Coloque a travessa de lasanha para assar durante 20 minutos')

escolha = int(input('Qual sua escolha (1- Mostrar os ingredientes, 2- Preparando a Lasanha) = '))
if (escolha==1):
        ingredientes_lasanha()
else:
    fogao()
    montagem_forma()
    forno()
