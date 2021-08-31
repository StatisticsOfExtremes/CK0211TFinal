import csv
import sys
import shutil

"""
NOME | IDADE | PORTE | RACA | LTEMP | RESPON | DATAADOCAO

"""

animal = {
    'id': '',
   'nome' : 'ROBERTO',
   'idade' : 35,
   'porte' : 'G',
   'raca': 'SRD',
   'ltemp': 'SÃO',
   'respon': '',
   'dataadocao': '25/08/2012'
}

animal2 = {
    'id': '',
   'nome' : 'JUNIOR',
   'idade' : 12,
   'porte' : 'G',
   'raca': 'ROTTWAILER',
   'ltemp': 'SÃO LASARO',
   'respon': 'JUNIM',
   'dataadocao': '25/08/2012'
}

animal3 = {
    'id': '',
   'nome' : 'GIGANTE',
   'idade' : 35,
   'porte' : 'G',
   'raca': 'SRD',
   'ltemp': 'SÃO',
   'respon': '',
   'dataadocao': '25/09/2021'
}


animal4 = {
    'id': '',
   'nome' : 'TOTORO',
   'idade' : 35,
   'porte' : 'G',
   'raca': 'SRD',
   'ltemp': 'SÃO',
   'respon': '',
   'dataadocao': '25/09/2021'
}   


filename = 'teste.csv'

fieldnames = ['id', 'nome', 'idade', 'porte', 'raca', 'ltemp', 'respon', 'dataadocao']


def checaCabecario(arquivo, fieldnames):
    with open(file=arquivo, encoding='utf-8') as f:
        linhas= f.readlines()[0]
        
        print(linhas)
        
        #if linhas != ''.join(fieldnames):
            #writer = csv.DictWriter(outputFile, fieldnames)
            #writer.writeheader()
        


"""
Abre a instancia do banco de dados como um dicionário
as primeiras linhas do banco são o cabeçário e se mantem
imutaveis pelo método DictWriter.
"""
def novoAnimal(arquivo, animal, fieldnames):
   with open(file=arquivo, mode='a',  newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames)
        checaCabecario(arquivo, fieldnames)
        try:
            novo_id = int(getLastRow(arquivo)[0]) + 1 #getLastRow retorna uma lista com os dados da ultima linha, a primeira é o id
            #Caso dê erro, é provavel que seja o primeiro valor da base, então:
        except:
            novo_id = 1
        animal['id'] = novo_id
        writer.writerow(animal)


"""
Aqui nos podemos ver o downside de usar csv, para modificar uma linha
devemos reescrever todo o arquivo
"""
def mudarDadosAnimal(arquivo, fieldnames, id_animal, novoAnimal):
    with open(file=arquivo, mode = 'r', encoding='utf-8', newline='') as inputFile, open(file='novoArquivo.csv', mode='w', encoding='utf-8', newline='') as outputFile:
        reader = csv.DictReader(inputFile, fieldnames)
        writer = csv.DictWriter(outputFile, fieldnames)

        for linha in reader:
            if linha['id'] == str(id_animal):
                novoAnimal['id'] = id_animal #Atualiza o id para o animal antigo
                print(novoAnimal)
            else:
                print(linha)

        shutil.move(arquivo, 'novoArquivo.csv')

def getLastRow(arquivo):
    with open(arquivo, mode='r', newline='', encoding='utf-8') as f:
        ultima_linha = f.readlines()[-1]
        return ultima_linha


novoAnimal(filename,animal, fieldnames)
novoAnimal(filename,animal2, fieldnames)
novoAnimal(filename,animal3, fieldnames)

#mudarDadosAnimal(filename, fieldnames, '3', animal4)