from funcoes import *
import emoji

geralAlunos=[]

print(emoji.emojize("PROGRAMA PRINCIPAL :Santa_Claus:"))
while True:
    print("1 - Cadastrar alunos e notas")
    print("2 - Exibir relatório")
    print("0 - Sair")

    escolha=int(input("Faça sua escolha : "))
    if escolha==1:
        nomeAluno=str(input("Digite o nome do aluno: "))
        nota1=int(input(f"Agora digite a nota 1 do aluno {nomeAluno}: "))
        nota2=int(input(f"Agora digite a nota 2 do aluno {nomeAluno}: "))
        nota3=int(input(f"Agora digite a nota 3 do aluno {nomeAluno}: "))
        listaNotas=[nota1,nota2,nota3]
        alunoMedia= calcular_media(listaNotas)
        situacao=verificar_situacao(alunoMedia)
        alunoRelatorio= [{nomeAluno: listaNotas},{"media": alunoMedia},{"situação":situacao}]
        geralAlunos.append(alunoRelatorio)

    elif escolha==2:
        print(geralAlunos)

    elif escolha==0:
        break