print('\n Bem vindos ao Bala Halls Club!\n')

nome= input('Digite seu nome:\n ')

estudante_py = input(f'\nVocê é estudante de Python? \nDigite "sim", ou "não": \n-')

idade= int(input('\nDigite sua idade: \n- '))

if idade >= 18 and estudante_py == 'sim':
    print('\nEscolha seu ingresso: \n1. Entrada Padrão : R$17,50 \n2.    VIP: R$30,00')
    input('Digite 1 ou 2: \n- ')
    print('\nCompra feita. Divirta-se!\n')

else: 
    if not idade< 18 and estudante_py == 'sim':
        print('\nEscolha seu ingresso: \n1. Padrão: R$35,00 \n2.   VIP:R$60,00')
        input('Digite 1 ou 2:\n- ')
        print('\n Compra feita. Divirta-se!\n')

    elif idade < 18:
        ano = 'anos'
        if idade == 1:
            ano = 'ano'
        print(f'Faltam {18 - idade} {ano} para você ter acesso ao club.')
