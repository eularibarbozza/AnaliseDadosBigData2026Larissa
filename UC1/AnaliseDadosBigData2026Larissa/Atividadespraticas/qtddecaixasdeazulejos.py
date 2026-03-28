###         Quantidade de Caixas de Azulejos: 
##      Use if/elif/else e/ou match/case para resolver os desafios abaixo:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, 
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em 
# todas as suas paredes (considere que não será descontada a área ocupada por portas e 
# janelas). Cada caixa de azulejos possui 1,5 m² 

caixa_de_azulejos=1.5
comprimento=None
largura=None
altura=None

try:
    comprimento=float(input("Informe o comprimento:"))
    largura=float(input("Informe a largura:"))
    altura=float(input("Informe a altura:"))
    dimensoes=2*comprimento*altura+2*largura*altura
    
    if comprimento >0 and largura >0 and altura >0:
        print("Dimensões da cozinha:",dimensoes)
        print("Caixas de pisos necessárias:",dimensoes/caixa_de_azulejos)
        print("Cálculo feito com sucesso!")
    

    elif comprimento <=0 or largura <=0 or altura <=0:
        print("Erro de medidas.")

except ValueError:
    print("Tente novamente.")