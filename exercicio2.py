"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('Que horas são? Digite no formato "00:00"')

try: 
    horario_int = int(horario[0:2:])

    if horario_int < 12:
        print('Bom dia')
    elif horario_int < 18:
        print('Boa tarde')
    elif horario_int < 24:
        print('Boa noite')
    else:
        print('Digite um horário válido.')
except:
        print('Digite um horário válido')