'''

CRUD

Açai

um aplicativo fast food, onde voce pode pedir sua sobremesa, personalizar o seu açai, efetuar o seu pagamento
e acompanhar o seu pedido

'''

print('\n=== SITE AÇAI===')
print('1. Fazer Pedido')
print('2. Ver Meus Pedidos')
print('3. Mudar Pedido')
print('4. Cancelar Pedido')
print('5. Relátorio do Pedido')
print('0. Sair')

while True: 

    escolha_cliente = input('O que você deseja fazer?')

    if escolha_cliente == '1':
        print('Vamos começar o seu pedido!')

        nome_cliente = input('Digite seu nome:')
        print('Aqui está o cardápio.')

        print('1 - Açai 300ml (10R$)')
        print('2 - Açai 500ml (20R$)')
        print('3 - Açai 1L (30R$)')

        pedido_cliente = input('Qual número do cardápio você gostaria de pedir? ')

        if pedido_cliente == '1':
            print('Você escolheu o açai de 300ml.')

        elif pedido_cliente == '2':
            print('Você escolheu o açai de 500ml.')

        elif pedido_cliente == '3':
            print('Você escolheu o açai de 1 litro.')

        else:
            print('Você escolheu uma opção invalida.')

        forma_pagamento = input('Qual será a forma de pagamento?')

        endereco_cliente = input('Nos informe em qual endereço será entregue o pedido: ')
        
        confirmar_endereco = input(f'O endereço: {endereco_cliente} está correto?')

        if confirmar_endereco == 'sim':
            print('Seu Pedido foi confirmado')
        else:
            print('Faça seu Pedido novamente.')
        break

    elif escolha_cliente == '2':
        print('Aqui esta seus pedidos:')

    elif escolha_cliente == '3':
        mudar_pedido = input('Oque você deseja mudar no seu pedido?')
        confirmar_pedido = input(f'Você modificou isto: {mudar_pedido}?')

        if confirmar_pedido == 'sim':
            print('Seu Pedido foi modificado com sucesso!')

        else:
            print('Tente novamente retornando ao menu.')
            continue

    elif escolha_cliente == '4':
        cancelar_pedido = input('Você gostaria de cancelar seu pedido?')

        if cancelar_pedido == 'sim':
            print('Seu Pedido foi cancelado com sucesso!')

        else:
            print('Seu Pedido não foi cancelado.')

    elif escolha_cliente == '5':
        print('Aqui está o relátorio do seu pedido:')

        

    elif escolha_cliente == '0':
        print('Saindo do Site. Volte Sempre!')
        break
    
    else:
        print('Opção invalida. Por favor tente novamente.')

