nota_matematica = input("Qual sua nota em matemática?")
nota_biologia = input("Qual sua nota em biologia?")
nota_portugues= input("Qual sua nota em português?")

soma = int(nota_matematica)+int(nota_biologia)+int(nota_portugues)
media = soma/3

print(media)

if media >= 5:
    print ("Você foi aprovado!")

else:
    print ("Você precisa estudar mais")
