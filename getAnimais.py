import time
from globalOpt import limparTela, renderBackground
"""
Cada animal deve conter um registro informando o seu nome; a idade (em
meses), o porte (pequeno, médio e grande); a raça (caso não houver será ‘sem
raça definida’ - SRD); o lar temporário, onde o animal está ou esteve antes de
ser adotado; o nome do responsável pela adoção; e a data de adoção. Para um
animal que ainda não foi adotado os campos de “responsável” e “data de
adoção” devem ficar vazios.

"""
def addAnimal():
    nomeAnimal = getData("Nome do Animal: ", 'str')
    idadeAnimal = getData("Idade (em meses): ", 'int')
    racaAnimal = getData("Raça: ", 'str')
    nomeLar = getData("Lar temporário: ", 'str')
    responsavel = getData("Responsável (Caso não tenha, deixar em branco): ", 'str')
    dataAdocao = getData("Data da adoção(Caso não tenha, deixar em branco): ", 'str')

    ##inserirAnimal(nomeAnimal, racaAnimal, nomeLar, responsavel, dataAdocao)


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
        renderBackground()
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
        renderBackground()
        return

def getData(Texto, Esperado):
    while True:
        try:
            if Esperado == "int":
                valor = int(input(Texto))
                break
            elif Esperado == "str":
                valor = input(Texto)
                break
            elif Esperado == "flt":
                valor = float(input(Texto))
                break
        except ValueError:
            print("O tipo do valor inserido não corresponde ao esperado, por favor tente novamente")
        
        except TypeError:
            print("O tipo de valor inserido está incorreto")

    return valor
    
