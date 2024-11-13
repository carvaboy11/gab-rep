def calcular_13_salario(salario_mensal, meses_trabalhados):
    # Cálculo do valor bruto do 13º salário
    valor_bruto = (salario_mensal / 12) * meses_trabalhados
    
    # Primeira parcela (50% do valor bruto)
    primeira_parcela = valor_bruto / 2
    
    # Cálculo do desconto de INSS (faixas de contribuição em 2024)
    if valor_bruto <= 1320.00:
        inss = valor_bruto * 0.075
    elif valor_bruto <= 2571.29:
        inss = valor_bruto * 0.09
    elif valor_bruto <= 3856.94:
        inss = valor_bruto * 0.12
    elif valor_bruto <= 7507.49:
        inss = valor_bruto * 0.14
    else:
        inss = 7507.49 * 0.14  # Teto máximo de contribuição

    # Cálculo da segunda parcela (bruto - INSS)
    segunda_parcela = (valor_bruto / 2) - inss
    
    # Cálculo do 13º total
    decimo_terceiro_total = primeira_parcela + segunda_parcela

    # Resultados
    print(f"Salário mensal: R${salario_mensal:.2f}")
    print(f"Meses trabalhados no ano: {meses_trabalhados}")
    print(f"Valor bruto do 13º salário: R${valor_bruto:.2f}")
    print(f"Primeira parcela: R${primeira_parcela:.2f}")
    print(f"Desconto de INSS: R${inss:.2f}")
    print(f"Segunda parcela: R${segunda_parcela:.2f}")
    print(f"Total a receber de 13º salário: R${decimo_terceiro_total:.2f}")

# Exemplo de uso
salario_mensal = float(input("Digite seu salário mensal (R$): "))
meses_trabalhados = int(input("Digite o número de meses trabalhados no ano (1 a 12): "))

calcular_13_salario(salario_mensal, meses_trabalhados)
