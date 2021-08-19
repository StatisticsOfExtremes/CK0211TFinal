import time
from globalOpt import limparTela
"""
Cada animal deve conter um registro informando o seu nome; a idade (em
meses), o porte (pequeno, médio e grande); a raça (caso não houver será ‘sem
raça definida’ - SRD); o lar temporário, onde o animal está ou esteve antes de
ser adotado; o nome do responsável pela adoção; e a data de adoção. Para um
animal que ainda não foi adotado os campos de “responsável” e “data de
adoção” devem ficar vazios.

"""
def addAnimal():
    nomeAnimal = input("Nome do Animal: ")
    idadeAnimal = int(input("Idade (em meses): "))
    racaAnimal = input("Raça: ")
    nomeLar = input("Lar temporário: ")
    responsavel = input("Responsável (Caso não tenha, deixar em branco): ")
    dataAdocao = input("Data da adoção(Caso não tenha, deixar em branco): ")


def modAnimal():
    codDel = int(input("Qual o código do bixinho para ser modificado? "))

def delAnimal():
    codDel = int(input("Qual o código do bixinho para ser deletado? "))

def listarAnimais():
    print("pega todos os bixos")

def opcoesMenuAnimais():
    opcao = input("""
    1 - Cadastrar novo animal
    2 - Modificar dados de um animal existente
    3 - Excluir dados de um animal existente
    4 - Voltar para o menu anterior
    """)
    if opcao == "1":
        limparTela()
        addAnimal()
        opcoesMenuAnimais()
    elif opcao == "2":
        print("Escolha o bixinho para modificar:")        
        limparTela()
        modAnimal()
        opcoesMenuAnimais()
    elif opcao == "3":
        limparTela()
        print("Escolha o bixinho para deletar:")
        time.sleep(3)
        listarAnimais()
        delAnimal()
        opcoesMenuAnimais()
    else:
        return