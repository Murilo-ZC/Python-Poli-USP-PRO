# Leitura de arquivos

nome_arquivo = "./minha_tabuada.csv"
print(f"Dados dentro do arquivo:{nome_arquivo}")
with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo.readlines():
        print("Linha:")
        elementos = linha.split(",")
        for i, item in enumerate(elementos):
            print(f"{i} - {item}")
            
            
            
            