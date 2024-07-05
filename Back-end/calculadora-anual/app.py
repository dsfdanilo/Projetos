def calcular_valor_com_desconto(valor_mensal):
    # Calcule o valor anual multiplicando por 12
    valor_anual = valor_mensal * 12

    # Defina a taxa de desconto como 15%
    taxa_desconto = 0.15

    # Calcule o valor anual com o desconto
    valor_anual_com_desconto = valor_anual * (1 - taxa_desconto)

    return valor_anual_com_desconto

# Solicite ao usuário o valor mensal
valor_mensal = float(input("Digite o valor mensal: "))

# Calcule o valor anual com desconto
valor_anual_com_desconto = calcular_valor_com_desconto(valor_mensal)

# Imprima o resultado
print(f"O valor mensal é: R$ {valor_mensal}")
print(f"O valor anual com 15% de desconto é: R$ {valor_anual_com_desconto}")
