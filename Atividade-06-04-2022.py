import pymongo
import pandas as pd

myclint = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclint["Atividade1"]
mycol = mydb["at1"]

#Fazer 3 prints as opções
print("Opcao 1 = Busca por (Place)")
print("Opcao 2 = Busca por Autor")
print("Opcao 3 = Busca por Data")

opcao = int(input("Digite sua opcao: "))

if opcao == 1:
    mydoc = mycol.find().sort("place",1)
    csv = pd.read_csv('C:/Users/gusta/OneDrive/Área de Trabalho/Projeto-Andre/ca-2004-01.csv','r')
    for y in csv:
        print(y)
    for x in mydoc:
     print(x)

if opcao == 2:
    mydoc = mycol.find().sort("author",1)
    csv = pd.read_csv('C:/Users/gusta/OneDrive/Área de Trabalho/Projeto-Andre/ca-2004-01.csv', 'r')
    for y in csv:
        print(y)
    for x in mydoc:
        print(x)

if opcao == 3:
    mydoc = mycol.find().sort("copyrightdate",1)
    csv = pd.read_csv('C:/Users/gusta/OneDrive/Área de Trabalho/Projeto-Andre/ca-2004-01.csv', 'r')
    for y in csv:
        print(y)
    for x in mydoc:
        print(x)


# opção para substituir swhitch case
# if nome_da_variavel == 1
# mostra os locais do rio de janeiro
# if nome_da_variavel == 2
# mostra as datas dos dados
# if nome_da_variavel == 3
# mostra o nome dos autores
# uma opção de saida