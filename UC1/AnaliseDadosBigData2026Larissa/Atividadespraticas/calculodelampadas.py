## Cálculo de Lâmpadas
#Use if/elif/else e/ou match/case para resolver os desafios abaixo:

# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.


# watts_por_metro=3
# largura=3
# comprimento=2
# dimensao=largura*comprimento
# numero_bocais=dimensao/3
# watts_total=dimensao*watts_por_metro
# numero_lampadas=watts_total/watts_por_metro


# if dimensao >=3 and watts_por_metro >=3 and numero_bocais !=0:
#     print("Cômodo iluminado!")
#     print("Quantidade de Watts:",watts_total)
#     print("Quantidade de lâmpadas:",numero_lampadas)

# elif numero_bocais <1 or watts_por_metro <3:
#     print("Cômodo sem luz!")

### Em aula


POTENCIA=3
largura=float(input("Largura:"))
comprimento=float(input("Comprimento:"))
area=largura*comprimento
lampadas=area/3

print(f"São necessarias {round(lampadas)} para iluminar um cômodo de {area} m2.")

