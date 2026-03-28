###         Média Escolar para 5 Estudantes 

#Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão 
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma 
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().

resultado=[]
notas_alunos=0
soma_total=0

for i in range(5):

    notas_alunos=float(input(f"Digite sua nota {i +1}:"))
    
    if notas_alunos >=6:
        resultado.append("Aprovado")
        print("Aprovado")
    
    else:
        resultado.append("Reprovado")
        print("Reprovado.")

    soma_total=soma_total+notas_alunos      

print(f"Média da turma: {soma_total/5}")
