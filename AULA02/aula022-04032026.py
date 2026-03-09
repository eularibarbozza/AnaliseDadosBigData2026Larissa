## Estruturas de decisão

chover=True
larissa_presenca=None

if chover==True:
    larissa_presenca=False
else:
    larissa_presenca=True

# Exercicio 1

placar_time1=0
placar_time2=3
resultado=None

if placar_time1>placar_time2:
    resultado='Time 1 ganhou!'
elif placar_time1<placar_time2:
    resultado='Time 2 ganhou!'
else:
    resultado='Empate!'