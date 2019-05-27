from .WriterAbstractFactory import WriterAbstractFactory

from writer.IWriterCashFlow import IWriterCashFlow
from writer.CSVWriterCashFlow import CSVWriterCashFlow

from writer.IWriterBankStatement import IWriterBankStatement
from writer.CSVWriteBankStatement import CSVWriterBankStatement

class CSVWriterFactory(WriterAbstractFactory):
    def createWriterBankStatement(self) -> IWriterBankStatement:
        return CSVWriterBankStatement()
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return CSVWriterCashFlow()