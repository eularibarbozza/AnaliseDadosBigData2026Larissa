###         Rendimento do Taxista:
##      Use if/elif/else e/ou match/case para resolver os desafios abaixo:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o 
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do 
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de 
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a 
# média do consumo em km/L e o lucro (líquido) do dia.

valor_do_combustivel=6.15
km_inicial=None
km_final=None
litros_de_combustivel=None
lucro_bruto=None

try:
    km_inicial=float(input("Digite a quilometragem inicial:"))
    km_final=float(input("Digite a quilometragem final:"))
    litros_de_combustivel=float(input("Digite a quantidade de gasolina utilizada:"))
    lucro_bruto=float(input("Informe o valor bruto faturado:"))

    if km_inicial >=0 and km_final>=km_inicial and litros_de_combustivel >0 and lucro_bruto >0:
        quilometragem_percorrida=km_final-km_inicial
        gasto_de_combustivel=litros_de_combustivel*valor_do_combustivel
        media=quilometragem_percorrida/litros_de_combustivel
        lucro_liquido=lucro_bruto-gasto_de_combustivel
        print("Sucesso na solicitação")
        print("Média de consumo de combustível:",media)
        print("Lucro líquido:",lucro_liquido)


        
    elif km_final<km_inicial or litros_de_combustivel <=0 or lucro_bruto <=0:
        print("Informe todas as opções solicitadas.")

except ValueError:
    print("Erro de digitação")
    print("Utilize: (.)")