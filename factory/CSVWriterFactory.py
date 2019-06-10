from .WriterAbstractFactory import WriterAbstractFactory

from writer.IWriterCashFlow import IWriterCashFlow
from writer.IWriterBankStatement import IWriterBankStatement
from writer.IWriterController import IWriterController

from writer.csv.CSVWriterCashFlow import CSVWriterCashFlow
from writer.csv.CSVWriteBankStatement import CSVWriterBankStatement
from writer.csv.CSVWriterController import CSVWriterController

class CSVWriterFactory(WriterAbstractFactory):
    def createWriterController(self) -> IWriterController:
        return CSVWriterController()

    def createWriterBankStatement(self) -> IWriterBankStatement:
        return CSVWriterBankStatement()
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return CSVWriterCashFlow()