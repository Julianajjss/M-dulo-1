nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?')

if idade >= 18
    print('Você pode ter acesso ao ingresso do clube de festas')
    print('-'*20)
    print('1- Entrada padrão\; R$35,00 \n2 - Entrada VIP: R$60,00')

    entrada = float(input('Escolha sua entrada:'))
    print('-'*20)
    print()
    print('-'*20)
    estuda = input('Você estuda Python?(sim ou nao)\n ')
    print('-'*20) 
    if estuda.lower() == 'sim':
        print('Você possui um desconto de 50%')
        if entrada == 1:
            print(f'Valor: R${35 * 0.5:.2f}')
        elif entrada == 2:
            print(f'Valor R${60 * 0.5:.2f}')
    else:
        print('Bem vindo(a), você recebeu sua entrada')
else:
    print('Espere mais {} ano(s) para entrar no clube!'. format(18 - idade))