# carro=True
# combustivel=True

#Qual a condição para que este carro funcione?


# if carro==True and combustivel==True: #<<<ambas as condições são verdadeiras!
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel=False:
#     print("Não sobrou nada para o fusquinha.")



# if carro==True and combustivel==True: #<<<ambas as condições são verdadeiras!
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada para o fusquinha.")
# else:
#     print("Erro de execução.")


# carro=False
# combustivel=False

# #          not(F)==Verdadeiro
# if not carro and not combustivel: #<<<ambas as condições são verdadeiras!
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada para o fusquinha.")
# else:
#     print("Erro de execução.")


#    Exemplo:
# semana = int(input("Informe o dia da semana"))
# if semana == 1:
#  print("Domingo")
# elif semana == 2:
#  print("Segunda-feira")
# elif semana == 3:
#  print("Terça-feira")
# elif semana == 4:
#  print("Quarta-feira")
# elif semana == 5:
#  print("Quinta-feira")
# elif semana == 6:
#  print("Sexta-feira")
# elif semana == 7:
#  print("Sábado")
# else: # O 'else' funciona como o 'default'
#  print("Dia inválido")


# # Match/Case (SEM tratamento de exceção!)

# mes=int(input("Informe o mês:"))
# match mes:
#     case 1:
#         print("Janeiro")
#     case 2:
#         print("Fevereiro")
#     case 3:
#         print("Março")
#     case 6:
#         print("Junho")
#     case _: # O underline ( _ ) funciona como o 'default' ou 'else'
#         print("Mês inválido")


# # Match/Case 

# try:

#     mes=int(input("Informe o mês:"))
#     match mes:
#         case 1:
#             print("Janeiro")
#         case 2:
#             print("Fevereiro")
#         case 3:
#             print("Março")
#         case 4:
#             print("Abril")
#         case 5:
#             print("Maio")
#         case 6:
#             print("Junho")
#         case 7:
#             print("Julho")
#         case 8:
#             print("Agosto")
#         case 9:
#             print("Setembro")
#         case 10:
#             print("Outubro")
#         case 11:
#             print("Novembro")
#         case 12:
#             print("Dezembro")

#         case _: # O underline ( _ ) funciona como o 'default' ou 'else'
#             print("Mês inválido")

# except ValueError:
#     print("Entrada inválida. Por favor, digite um número inteiro.")
# except ZeroDivisionError:
#     print("Código inválido. Esqueceu da identação?")




#Range 

# intervalo1=range(10)
# print(intervalo1)

# print("***")

# for numero in range(10):
#         print("Número:")
#         print(numero)

# for numero in range(1,10,3):
#         print("Número:")
#         print(numero)

