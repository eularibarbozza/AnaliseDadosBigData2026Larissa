## Cálculo de Lâmpadas
#Use if/elif/else e/ou match/case para resolver os desafios abaixo:

# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.


potencia=3
largura=3
comprimento=2
dimensao=largura*comprimento

if potencia >=3 and dimensao >=3:
    print("Casa iluminada")

elif potencia <3 and dimensao >=3:
    print("Watts inferior")
