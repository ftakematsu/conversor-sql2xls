import mysql.connector

class Database:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="backup_integralsaude"
        )
        self.cursor = self.conexao.cursor()
    
    def tipoAtributo(self, atributo):
        if (atributo==("IDPAIS")):
            return "VARCHAR(10)"
        if (atributo=="ID" or atributo.startswith("ID") or atributo=="EMPRESA"):
            return "INT"
        elif (atributo.startswith("DT") or atributo.startswith("DATA")):
            return "DATETIME"
        elif (atributo=="LOG_UPDATE" 
              or atributo.startswith("ATIVIDADES") 
              or atributo=="LTCATOBS" 
              or atributo=="DESCRICAO"
              or atributo=="LEGENDAANALISERISCOS"
              or atributo=="EVENTOS_ESOCIAL"
              or atributo=="DENOMINACAO"
              or atributo=="PCMSOOBS"):
            return "TEXT"
        elif (atributo=="RAZAOSOCIAL" or atributo=="EMAIL"):
            return "VARCHAR(100)"
        else:
            return "VARCHAR(50)"

    def criaAtributos(self, atributos):
        lista = ""
        for index, atributo in enumerate(atributos):
            if (index<len(atributos)-1):
                lista += atributo + " " + self.tipoAtributo(atributo) + ", "
            else:
                lista += atributo + " " + self.tipoAtributo(atributo)
        return lista

    def criarTabela(self, name, atributos):
        #atributos = "id INT, name VARCHAR(255), address VARCHAR(255)"
        #print(self.criaAtributos(atributos))
        sqlQuery = f"CREATE TABLE IF NOT EXISTS {name}(CODIGO INT NOT NULL AUTO_INCREMENT, {self.criaAtributos(atributos)}, PRIMARY KEY(CODIGO))"
        print(sqlQuery)
        self.cursor.execute(sqlQuery)
    
    def inserirRegistro(self, sql):
        if (sql.startswith("INSERT")):
            #print(sql)
            self.cursor.execute(sql)
            self.conexao.commit()
            print(self.cursor.rowcount, "record inserted.")
        
    def buscarDados(self, sql):
        if (sql.startswith("SELECT")):
            self.cursor.execute(sql)
            return self.cursor.fetchall()


