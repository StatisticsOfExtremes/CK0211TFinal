import os

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
    commando = 'clear'
    if os.name in ('nt', 'dos'):  # Se tiver usando o windows o comando para limpar a tela é 'cls'
        commando = 'cls'
    os.system(commando)

def renderBackground():
        limparTela()
        print(welcomeStr)

