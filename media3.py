print('Consulte sua Média Escolar')

nota1 = int(input('Insira sua nota na disciplina de Português: '))
nota2 = int(input('Insira sua nota na disciplina de Matemática: '))
nota3 = int(input('Insira sua nota na disciplina de História: '))
nota4 = int(input('Insira sua nota na disciplina de Geografia: '))
nota5 = int(input('Insira sua nota na disciplina de Biologia: '))

media_total = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

def notas ():
    if media_total <= 4:
        print('Sua média é : {media_total}, Você está Reprovado.')
    
    elif media_total >= 7:
        print('Sua média é: {media_total}, Parabéns, Você está Aprovado!')

    else:
        print('Sua média é: {media_total}, Você está de Recuperação.')

notas()