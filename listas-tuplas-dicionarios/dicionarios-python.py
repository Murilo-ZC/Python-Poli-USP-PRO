# Dicionários

pontos = {}

pontos["vitorias"] = 3
pontos["derrotas"] = 2
pontos["empates"] = 0

# Exibe os dados dentro do dicionário
print(pontos)

# Adicionando mais valor em uma das chaves
pontos["vitorias"] += 1

# Passando por todos os valores do dicionário
for chave, valor in pontos.items():
    print("Chave:", chave, "Valor:", valor)
    
    
    