from globalOpt import limparTela, renderBackground

def opcoesMenuCandidato():
    opcao = input("""
    1 - Cadastrar novo candidato
    4 - Voltar para o menu anterior
    """)

    if opcao == "1":
        limparTela()
        addCandidato()
    else:
        renderBackground()
        return


def addCandidato():
    condFinan = input("Você possui condições financeiras para adotar um novo animal? (Sim/Não)")
    tempoLivre = input("Avaliando sua rotina, você possui tempo livre para se dedicar ao seu novo pet? (Sim/Não)")
    porteMax = input("Pense agora no espaço que você possui em casa:\n qual o porte máximo que o animal deverá ter para viver confortavelmente com você?(Pequeno/Médio/Grande)")

