print ('Situação do Aluno')

def notas(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    print (f'Sua média é media,2)!')
    if media >= 7:
        print('Parabéns,você está aprovado.')
    elif media >= 4 and media <= 7 :
        print('\nVocê está de recuperação. Você precisa tirar', round (10 - media,2),' na prova final.')
    else :
        print('Você está REPROVADO!')
    
mat = input('Qual é sua nota em Matemática?')
port = input ('Qual é sua nota em Português?')
bio = input ('Qual é sua nota em Biologia?')

notas(9,8,7)