## Cálculo de Lâmpadas
#Use if/elif/else e/ou match/case para resolver os desafios abaixo:

# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.

watts_por_metro=3
largura=3
comprimento=2
dimensao=largura*comprimento
numero_bocais=dimensao/3
watts_total=dimensao*watts_por_metro
numero_lampadas=watts_total/watts_por_metro


if dimensao >=3 and watts_por_metro >=3 and numero_bocais !=0:
    print("Cômodo iluminado!")
    print("Quantidade de Watts:",watts_total)
    print("Quantidade de lâmpadas:",numero_lampadas)

elif numero_bocal <1 or watts_metro <3:
    print("Cômodo sem luz!")