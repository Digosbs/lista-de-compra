while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operacao = input('Digite o operador (+-/*): ')

    if numero_1.isdigit() and numero_2.isdigit():
        numero_1_float = int(numero_1)
        numero_2_float = float(numero_2)

        if (operacao == '+') or (operacao == '-') or (operacao == '/') or (operacao == '*'):
            if operacao == '+':
                print(f'a soma de {numero_1} com {numero_2} é: {numero_1_float + numero_2_float}')
            elif operacao == '-':
                print(f'a subtração de {numero_1} com {numero_2} é: {numero_1_float - numero_2_float}')
            elif operacao == '/':
                print(f'a divisão de {numero_1} com {numero_2} é: {numero_1_float / numero_2_float}')
            elif operacao == '*':
                print(f'a multiplicação de {numero_1} com {numero_2} é: {numero_1_float * numero_2_float}')
        else:
            print('Não foi digitado uma operação válida')
    else:
        print('Não foi digitado número')


    sair = input('Quer [s]air?: ').lower().startswith('s')
    if sair is True:
        break