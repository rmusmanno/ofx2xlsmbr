from .WriterAbstractFactory import WriterAbstractFactory

from writer.IWriterCashFlow import IWriterCashFlow
from writer.CSVWriterCashFlow import CSVWriterCashFlow

from writer.IWriterBankStatement import IWriterBankStatement
from writer.CSVWriteBankStatement import CSVWriterBankStatement

from writer.IWriterController import IWriterController
from writer.CSVWriterController import CSVWriterController

class CSVWriterFactory(WriterAbstractFactory):
    def createWriterController(self) -> IWriterController:
        return CSVWriterController()

    def createWriterBankStatement(self) -> IWriterBankStatement:
        return CSVWriterBankStatement()
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return CSVWriterCashFlow()