lista = []

while True:
    print('Selecione uma opçao')
    escolha = input('[I]nserir [A]pagar [L]istar: ')

    if len(escolha) == 1:
        if escolha.lower() == 'a':
            lista_enumerada = enumerate(lista)
            for item in lista_enumerada:
                print(item)
            item_escolhido = input('Qual item deseja excluir?: ')
            lista.pop(int(item_escolhido))
        elif escolha.lower() == 'i':
            novo_item = input('O que deseja inserir na sua lista de compras?: ')
            insira = lista.append(novo_item)
            
        elif escolha.lower() == 'l':
            if len(lista) == 0:
                print('Não contém nenhum item na sua lista.')
            else:
                lista_enumerada = enumerate(lista)
                for item in lista_enumerada:
                    print(item)
        else:
            print('Opção inválida, digite "I" para inserir, "A" para apagar ou "L" para listar')




        
    else:
        print('Digite apenas uma letra')
