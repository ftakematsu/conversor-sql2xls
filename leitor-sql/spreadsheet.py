import xlsxwriter


class Excel:
    def __init__(self, dataAtual=""):
        dir = f'backup-integral-{dataAtual}.xlsx'
        self.workbook = xlsxwriter.Workbook(dir)
        self.worksheet = self.workbook.add_worksheet('Modelo planilha')
        print(f"Criado: {dir}")

    def SQL2XLS(self, queryResult):
        self.worksheet.write('A1', 'Hello..')
        self.worksheet.write('B1', 'Geeks')
        self.worksheet.write('C1', 'For')
        self.worksheet.write('D1', 'Geeks')
        self.workbook.close()
        