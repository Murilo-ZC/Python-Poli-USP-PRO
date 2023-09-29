# Tuplas
valores = (1,2,3,4,5,6,-4,8)

# Acessando um valor da tupla
print(valores[0])

# Trocando um valor da tupla
valores[1] = 45

# Encontrando o maior valor da tupla
print("Maior valor da tupla:", max(valores))

# Menor valor
print("Menor valor da tupla:", min(valores))

# Valor médio
print("Média da tupla:", sum(valores)/len(valores))

# Passa por todos os valores da tupla
for valor in valores:
    print(valor)

