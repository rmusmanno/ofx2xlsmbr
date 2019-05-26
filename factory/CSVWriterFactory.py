from .WriterAbstractFactory import WriterAbstractFactory

class CSVWriterFactory(WriterAbstractFactory):
    def createWriterBankStatement(self) -> IWriterBankStatement:
        #return CSVWriterBankStatement
        pass

    def createWriterCashFlow(self) -> IWriterCashFlow:
        #return CSVWriterCashFlow
        pass