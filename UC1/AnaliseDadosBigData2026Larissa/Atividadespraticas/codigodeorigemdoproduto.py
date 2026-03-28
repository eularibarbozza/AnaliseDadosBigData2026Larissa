####            Código de Origem do Produto
##      Use if/elif/else e/ou match/case para resolver os desafios abaixo:
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região 
# de sua procedência, conforme a tabela abaixo:
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser 
# encarado como “Importado”.

# codigo1=sul
# codigo2=norte
# codigo3=leste
# codigo4=oeste
# codigo5|6=nordeste
# codigo7|8|9=sudeste
# codigo10=centro_oeste
# codigo11=noroeste

try:

    regiao=int(input("Informe o código de origem do produto:"))
    match regiao:
        case 1:
            print("Sul")
        case 2:
            print("Norte")
        case 3:
            print("Leste")
        case 4:
            print("Oeste")
        case 5|6:
            print("Nordeste")
        case 7|8|9:
            print("Sudeste")
        case 10:
            print("Centro-Oeste")
        case 11:
            print("Noroeste")
            
        case _:
            print("Importado")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")