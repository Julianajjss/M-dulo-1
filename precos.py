print('Vamos fazer compras!')
print('Escreva o nome de três produtos de \nmercado e seus respectivos preços')
produto1 = input('\n1º Produto: ')
produto1_preco = float(input('     Preço:'))

produto2 = input('\n2º Produto: ')
produto2_preco = float(input('     Preço:'))

produto3 = input('\n3º Produto: ')
produto3_preco = float(input('     Preço: '))

if produto1_preco < produto2_preco and produto2_preco < produto3_preco:
    print(f'{produto1} é o produto mais baraato.')

elif produto2_preco < produto1_preco and produto1_preco < produto3_preco:
    print(f'{produto2} é o produto mais barato.')

elif produto3_preco < produto1_preco and produto1_preco < produto2_preco:
    print(f'\n{produto3} é o produto mais barato. \n')
