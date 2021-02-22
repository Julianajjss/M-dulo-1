def multiplicar(multiplicando, multiplicador):
    x = int(multiplicando)
    y = int(multiplicador)
    if x > 50 or y > 50:
            print('\nErro: Insira números entre 1 e 50.\n')
    else:
            print('\nMultiplicando   \n')
            print(f'{x} x {y} = {x * y}\n')
            
print('\nInsira dois números entre 1 e 50 para serem multiplicados.')

multiplicando = input('\nMultiplicando: ')
multiplicador = input('\nMultiplicador: ')

multiplicar(multiplicando,multiplicador)