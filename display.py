import getAnimais
import getAdocao
import getCandidato
import os
import globalOpt

def getOptions():
        opcao = input("""
        1 - Cadastrar novos animais
        2 - Consultar animais
        3 - Adotar um animal
        """)
        if opcao == "1":
                globalOpt.renderBackground()
                getAnimais.opcoesMenuAnimais()
                getOptions()
        elif opcao == "2":
                globalOpt.renderBackground() 
                getAnimais.listarAnimais()
                getOptions()
        elif opcao == "3":
                globalOpt.renderBackground()
                #getAdocao
                getOptions()
            


def main():
    while True:
        getOptions()


main()


