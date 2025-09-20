print('===========******{ Sistema de Preços v1 }********===========')
input('Aperte qualquer tecla para continuar...')

# Dicionário de produtos com seus preços
produtos = {
    "maçã": "R$ 10,50",
    "banana": "R$ 8,00",
    "laranja": "R$ 9,50",
    "uva": "R$ 12,00",
    "melancia": "R$ 15,00",

    "leite": "4,99",
    "macarrao": "4,20"

}

# Exibe apenas os nomes das frutas (catálogo sem preços)
print('\n===== Catálogo de Frutas =====')
for fruta in produtos:
    print(f"- {fruta.capitalize()}")

print('\n===== Outros produtos =====')
for produtos in produtos:
    print(f"- {produtos.capitalize()}")
print('==============================\n')

# Solicita o nome do produto ao usuário
nome_produto = input('Digite o nome do produto desejado: ').lower()

# Verifica se o produto está na lista e mostra o preço
if nome_produto in produtos:
    print(f"\nO preço de {nome_produto.capitalize()} é {produtos[nome_produto]}")
else:
    print("\nProduto não encontrado.")
