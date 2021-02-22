def saude(exame):
    if exame >7:
        print('\nSua saúde está ótima,continue com os cuidados.')

    elif exame < 7 and exame >= 4 :
        print('\nSua saúde está mediana, busque se cuidar e fazer acompanhamento médico.')

    elif exame < 4:
        print('\nSua saúde não está boa, procure um médico.\n')


paciente1 = 7
paciente2 = 5
paciente3 = 3

saude(paciente1)

saude(paciente2)

saude(paciente3)
