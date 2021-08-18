import getCadastro
import getAnimais
import getAdocao
from os import system as sys

welcomeStr = """
   _____ _  _____    _____          _   _______ 
  / ____(_)/ ____|  / ____|   /\   | | |__   __|
 | (___  _| (___   | |  __   /  \  | |    | |   
  \___ \| |\___ \  | | |_ | / /\ \ | |    | |   
  ____) | |____) | | |__| |/ ____ \| |____| |   
 |_____/|_|_____/   \_____/_/    \_\______|_|   
                                                                                             
"""

print(welcomeStr)

def limparTela():
        sys('cls||clear')

def renderBackground():
        limparTela()
        print(welcomeStr)


def getOptions():
        opcao = input("""
        1 - Cadastrar novos animais
        2 - Consultar animais
        3 - Adotar um animal
        """)
        if opcao == 1:
                renderBackground()
                getCadastro()
                getOptions()
        elif opcao == 2:
                renderBackground() 
                getAnimais()
                getOptions()
        elif opcao == 3:
                renderBackground()
                getAdocao()
                getOptions()
            


def main():
    while True:
        getOptions()


main()


