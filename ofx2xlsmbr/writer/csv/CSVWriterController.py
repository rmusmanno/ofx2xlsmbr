import csv

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow

from writer.IWriterController import IWriterController

# Deprecado, provavelmente nao esta funcionando mais
class CSVWriterController(IWriterController):
    def write(self, data, factory, outputFilename):
        csvData = []

        writerBS = factory.createWriterBankStatement()
        writerBS.write(data, factory, csvData)

        with open(outputFilename + '.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)