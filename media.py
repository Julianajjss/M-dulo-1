def nome():
    nome= input('Digite seu nome: ')
    return nome 

def media(nota_py,nota_ingles,nota_mat):

    return (nota_py + nota_ingles + nota_mat)/3

aluno = nome()
nota_final = media(4,9,7)
print(f'Sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(6,7,10)
print(f'Sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(10,8,3)
print(f'Sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(10,5,8)
print(f'Sua média é {nota_final:.2f}.')

aluno = nome()
nota_final = media(10,9,10)
print(f'Sua média é {nota_final:.2f}.')

