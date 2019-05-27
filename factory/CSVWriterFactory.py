from .WriterAbstractFactory import WriterAbstractFactory

from writer.IWriterCashFlow import IWriterCashFlow
from writer.CSVWriterCashFlow import CSVWriterCashFlow

from writer.IWriterBankStatement import IWriterBankStatement
from writer.CSVWriteBankStatement import CSVWriterBankStatement

from writer.IWriter import IWriter
from writer.CSVWriter import CSVWriter

class CSVWriterFactory(WriterAbstractFactory):
    def createWriter(self) -> IWriter:
        return CSVWriter()

    def createWriterBankStatement(self) -> IWriterBankStatement:
        return CSVWriterBankStatement()
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return CSVWriterCashFlow()