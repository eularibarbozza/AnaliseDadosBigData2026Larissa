#Limpar os dados da mesa e a torna disponivel para o proximo cliente.


import random 

def limpar_mesa(finalizar_caixa,consumo_total):
    """
    Limpa os dados de consumo e redefine o status da mesa para disponível.
    """
    mesapaga=finalizar_caixa
 
    if consumo_total == mesapaga:
        status_mesa = "Disponível"
        print("Mesa limpa e pronta para o próximo cliente!")
    else:
        print(f"Erro: Ainda há um débito de R${consumo_total:.2f}. Finalize o pagamento antes de limpar.")
    
    return status_mesa

---------------------------------------------------------------------------------------------------------------------------------------------------------------
# AÇÃO 09 – LARISSA

# Melhorias importantes:
# - A lógica de liberar estava correta, mas a comparação estava equivocada (comparava com 'False' quando deveria ser 'True').
# - O main chama pelo nome de função liberar_mesa(), então renomeei e adaptei.
# - Removidos parâmetros e adicionado input para o número da mesa, garantindo que a função seja mais flexível e fácil de usar.
from acao02 import mesas_restaurante

def liberar_mesa():
    """
    Libera a mesa após o pagamento.
    """

    numero = input("Digite o número da mesa a liberar: ")

    identificador = f"Mesa {numero}"

    # Isto daqui garante que a mesa exista (uma boa prática adicionada)
    if identificador not in mesas_restaurante:
        print("Mesa inexistente.")
        return

    # Lógica original “limpar a mesa” correta e foi mantida:
    mesas_restaurante[identificador] = True  # 'True' significava “disponível” no seu código

    print(f"A {identificador} foi limpa e está disponível novamente!")
