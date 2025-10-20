from funcoes import *

alunosNomes=[]

print("PROGRAMA PRINCIPAL")
while True:
    print("1 - Cadastrar alunos e notas")
    print("2 - Exibir relatório")
    print("0 - Sair")

    escolha=int(input("Faça sua escolha: "))
    if escolha==1:
        aluno=str(input("Digite o nome do aluno: "))