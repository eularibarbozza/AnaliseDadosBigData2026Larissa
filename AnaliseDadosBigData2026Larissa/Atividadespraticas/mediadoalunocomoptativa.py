####            Média do Aluno com Optativa:
##      Use if/elif/else e/ou match/case para resolver os desafios abaixo:
# Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
# substitui a nota mais baixa entre as duas primeiras avaliações.
# 
# Escrever a média e
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
# recuperação, de acordo com as informações abaixo:

# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.0

nota01=float(input("Primeira nota:"))
nota02=float(input("Segunda nota:"))
nota_opt=float(input("Tem nota optativa?:"))


if nota_opt == -1:
    media=(nota01+nota02)/2

else:
    if nota_opt > nota01:
        media=(nota_opt+nota02)/2
    else:
        media=(nota_opt+nota01)/2


if media >= 6.0:
    resultado="Aprovado"
elif media >=3.0:
    resultado="Recuperação"
else:
    resultado="Reprovado"

print(f"Média final:{media};Resultado:{resultado}")




