"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome.')
if len(primeiro_nome) < 5:
    print('Seu nome é pequeno')
elif len(primeiro_nome) < 7:
    print('Seu nome é médio')
else:
    print('Seu nome é grande')

    