import random

# Gera 15 números aleatórios de 01 a 25
numeros = random.sample(range(1, 26), 15)

# Ordena os números em ordem crescente
numeros_ordenados = sorted(numeros)

# Imprime os resultados
print("Números ordenados:", numeros_ordenados, "Boa sorte! :)")
