# Inputs  

email = input("Escreva seu e-mail: ")
nome = input("Seu primeiro nome: ")

print(email, nome)
print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmação")

# faturamento = float(input("Escreva o faturamento: "))

# imposto = faturamento * 0.1

# print(imposto)
print('-' * 100)

# Listas
vendas = [100, 50, 14, 20, 30, 700]

# soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

# tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# max e min
print(max(vendas))
print(min(vendas))

# pegar posição
print(vendas[0])
print(vendas[-1])
print(vendas[2])

lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

# produto_procurado = input("Pesquise pelo nome do produto: ")
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in lista_produto)

# print("apple watch" in lista_produto)
# print("iphone" in lista_produto)clip

# adicionar um item
lista_produtos.append("apple watch")
print(lista_produtos)

# remover um item
lista_produtos.remove("apple watch")
print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)

# editar um item
precos = [1000, 1500, 3500]
precos[0] = 6000
precos[0] = precos[0] * 1.5
print(precos)


# contar quantas vezes um item aparece na lista
lista_produtos = ["iphone", "airpode", "macbook", "iphone", "ipad", "iphone"]
print(lista_produtos.count("iphone"))

# ordenar uma lista
lista_produtos.sort()
# lista_produtos.sort(reverse=True)
print(lista_produtos)

vendas.sort(reverse=True)
print(vendas)

