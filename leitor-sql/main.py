import os 

path = "/Users/imac1apucarana/Documents/Workspace/backup-integral/database"
os.chdir(path)
#print("Lendo arquivos em ", os.listdir())

def removeColchetes(palavra):
    return palavra.replace("[", "").replace("]","")

def criarTabela(sql):
    nome_tabela = sql.split("INSERT INTO",1)[1].split("([")[0]
    nome_tabela = removeColchetes(nome_tabela.strip())
    print("Criando tabela", nome_tabela)

def lerArquivo(file_path):
    with open(file_path, 'r') as file:
        #print(file)
        listaComandos = file.readlines()
        criarTabela(listaComandos[0])

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
    while (i<len(file_list) and not file_list[i].endswith(name)):
        i +=1
    return file_list[i]

def testeArquivo():
    file_list = setFileList()
    file = searchFileByName("USUARIOS.sql", file_list)
    lerArquivo(file)
    

def processarTodosArquivos():
    file_list = setFileList()
    print("ARQUIVOS LIDOS ", len(file_list))
    #for file_path in file_list:
    #    lerArquivo(file_path)



if __name__=="__main__":
    processarTodosArquivos()
    #testeArquivo()
