# Escrita de arquivos

nome_arquivo = "./minha_tabuada.csv"

arquivo = open(nome_arquivo, "w")
for numero in range(100):
    saida = ""
    for i in range(1, 11):
        saida +=f"{numero*i},"
    saida= saida[:-1]+"\n"
    arquivo.write(saida)

        