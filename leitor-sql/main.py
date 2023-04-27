import os
from database import *
from spreadsheet import *

#path = "/Users/imac1apucarana/Documents/Workspace/backup-integral/database"
path = "D:/workspace/conversor-sql2xls/backup"
os.chdir(path)
#print("Lendo arquivos em ", os.listdir())
dataBackup = "2023-04-19"

# Database
db = Database()

# Excel
excel = Excel(dataBackup)

def removeColchetes(palavra: str):
    return palavra.replace('[', "").replace(']',"")

def removeColchetesSQL(sql: str):
    index = sql.find('VALUES(')
    return removeColchetes(sql[:index]) + sql[index:]

def setFileList():
    file_list = []
    # Iterate over all the files in the directory
    for file in os.listdir():
        # Create the filepath of particular file
        file_path =f"{path}/{file}"
        file_list.append(file_path)
    return file_list

def searchFileByName(name, file_list):
    i=0
    while (i<len(file_list) and not file_list[i].endswith("/" + name)):
        i +=1
    #print("Encontrado: " + file_list[i])
    return file_list[i]


    

def processarTodosArquivos():
    file_list = setFileList()
    print("ARQUIVOS LIDOS ", len(file_list))



def criarTabela(sql):
    nome_tabela = sql.split("INSERT INTO",1)[1].split('([')[0]
    nome_tabela = removeColchetes(nome_tabela.strip())
    #print("Criando tabela", nome_tabela)
    lista_atributos = sql.split(')  VALUES')[0].split('(')[1]
    lista_atributos = removeColchetes(lista_atributos)
    #print("Atributos", lista_atributos)
    db.criarTabela(nome_tabela, lista_atributos.split(","))


def lerArquivoEInserir(file_path):
    with open(file_path, encoding="utf8") as file:
        #print(file)
        listaComandos = file.readlines()
        criarTabela(listaComandos[0])
        # Realizar inserções na tabela
        comandoSql = ""
        i=0
        while (i<len(listaComandos)):
            # If is new insert command:
            if (listaComandos[i].startswith("INSERT INTO")):
                comandoSql = listaComandos[i]
            else: # if not, concatenate string with next
                comandoSql += listaComandos[i]
            i+=1               
            isInsert = False
            # is last or the next command is insert 
            if (i==len(listaComandos)): 
                isInsert = True
            elif (listaComandos[i].startswith("INSERT INTO")): # Not last
                isInsert = True
            # Verifica se vai inserir
            if (isInsert):
                db.inserirRegistro(removeColchetesSQL(comandoSql))

def escreverNaPlanilha():
    comandoSQLBusca = ""
    resultado = db.buscarDados(comandoSQLBusca)
    excel.SQL2XLS(resultado)


def processarTabela(arquivoSQL, insert=False):
    file_list = setFileList()
    file = searchFileByName(arquivoSQL, file_list)
    if (insert):
        lerArquivoEInserir(file)
    escreverNaPlanilha()

if __name__=="__main__":
    #processarTodosArquivos()
    #processarTabela("EMPREGADOS.sql",True)
    #processarTabela("CARGOS.sql",True)
    #processarTabela("SETORES.sql",True)
    processarTabela("EMPRESAS.sql", True)
