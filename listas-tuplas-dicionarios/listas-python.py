# Listas
valores = [1,2,3,4,5,6,-4,8]

# Acessando um valor da lista
print(valores[0])

# Trocando um valor da lista
valores[1] = 45

# Encontrando o maior valor da lista
print("Maior valor da lista:", max(valores))

# Menor valor
print("Menor valor da lista:", min(valores))

# Valor médio
print("Média da lista:", sum(valores)/len(valores))

# Passa por todos os valores da lista
for valor in valores:
    print(valor)

