<<<<<<< HEAD
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
        4 - Sair
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
        elif opcao == '4':
                return False
            


def main():
        open = True
        while open:
              open = getOptions()
              


main()


=======
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
        4 - Sair
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
        elif opcao == '4':
                return False
            


def main():
        open = True
        while open:
              open = getOptions()
              


main()


>>>>>>> master
