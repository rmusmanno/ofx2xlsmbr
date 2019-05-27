import csv

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow

from .IWriterController import IWriterController
from .IWriterCashFlow import IWriterCashFlow
from .CSVWriterCashFlow import CSVWriterCashFlow

class CSVWriterController(IWriterController):
    def write(self, data: BankStatement, factory, outputFilename):
        csvData = []

        writerBS = factory.createWriterBankStatement()
        writerBS.write(data, factory, csvData)

        with open(outputFilename + '.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)