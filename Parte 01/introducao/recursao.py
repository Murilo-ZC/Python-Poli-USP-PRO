# Recursão
def fibonacci(valor):
    if valor == 1:
        return 1
    elif valor == 0:
        return 0
    else:
        print(valor)
        return fibonacci(valor - 2) + fibonacci(valor - 1)

# Exibe o 5 valor da sequencia de Fibonacci
fibonacci(5)

