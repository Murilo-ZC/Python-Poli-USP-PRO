# Utilizando funções
def mostrarMenu():
    print("1 - Somar")
    print("2 - Substrair")
    print("0 - Sair")
    
def somar(num1, num2):
    return num1+num2

def subtrair(num1, num2):
    return num1-num2

def main():
    continuar = True
    while continuar:
        mostrarMenu()
        opcao = int(input("Escolha:"))
        if opcao == 1:
            num1 = int(input("Número 1:"))
            num2 = int(input("Número 2:"))
            print("Resultado:", somar(num1, num2))
        elif opcao == 2:
            num1 = int(input("Número 1:"))
            num2 = int(input("Número 2:"))
            print("Resultado:", subtrair(num1, num2))
        elif opcao == 0:
            continuar = False
        else:
            print("Opção Inválida!")
main()
