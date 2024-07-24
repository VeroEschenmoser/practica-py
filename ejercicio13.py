# Inicializar los primeros dos números de la serie Fibonacci
a, b = 0, 1

# Imprimir los primeros dos números de la serie Fibonacci
print(a)
print(b)

# Calcular e imprimir los siguientes 8 números de la serie Fibonacci
for i in range(3, 11):
    c = a + b
    print(c)
    a, b = b, c
