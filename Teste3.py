nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

# Link do cardápio e lista de bebidas
cardapio = 'www.adega.com.br'
bebidas_alcoolicas = 'Wisky, Vodka nacional, Vodka internacional, Tequila, Gin'

if idade >= 18:
    print(f'{nome}, seja bem-vindo!')
    ver_bebidas = input('Gostaria de ver as bebidas alcoólicas? (Sim/Não): ').strip().lower()
    if ver_bebidas == 'sim':
        print('Nossas bebidas alcoólicas: ' + bebidas_alcoolicas)
else:
    print(f'{nome}, para bebida temos sucos e refrigerantes.')

#----------------------------------------------------#

pedido = input('Já fez o seu pedido? (Sim/Não): ').strip().lower()

if pedido == 'sim':
    print('Bom apetite!')
else:
    ver_cardapio = input('Gostaria de ver o cardápio? (Sim/Não): ').strip().lower()
    if ver_cardapio == 'sim':
        print('Nosso cardápio: ' + cardapio)
