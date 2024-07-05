import csv

# Use strings raw (caminhos de arquivo com o prefixo r) para evitar erros de escape
caminho_entrada = r'C:\Users\danil\OneDrive\Área de Trabalho\Projetos\Limpar Coluna\nps.csv'
caminho_saida = r'C:\Users\danil\OneDrive\Área de Trabalho\Projetos\Limpar Coluna\teste.csv'

with open(caminho_entrada, 'r', newline='') as arquivo_entrada, open(caminho_saida, 'w', newline='') as arquivo_saida:
    leitor_csv = csv.reader(arquivo_entrada)
    escritor_csv = csv.writer(arquivo_saida)

    for linha in leitor_csv:
        nova_linha = []
        for celula in linha:
            posicao_inicial = 10
            nova_celula = celula[:posicao_inicial]
            nova_linha.append(nova_celula)

        escritor_csv.writerow(nova_linha)
