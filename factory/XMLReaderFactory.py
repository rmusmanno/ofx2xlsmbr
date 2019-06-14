from .ReaderAbstractFactory import ReaderAbstractFactory

from reader.IReaderCashFlow import IReaderCashFlow
from reader.IReaderBankStatement import IReaderBankStatement
from reader.IReaderController import IReaderController

from reader.xml.XMLReaderCashFlow import XMLReaderCashFlow
from reader.xml.XMLReaderBankStatement import XMLReaderBankStatement
from reader.xml.XMLReaderController import XMLReaderController

class XMLReaderFactory(ReaderAbstractFactory):
    def createReaderController(self) -> IReaderController:
        return XMLReaderController()

    def createReaderBankStatement(self) -> IReaderBankStatement:
        return XMLReaderBankStatement()
    
    def createReaderCashFlow(self) -> IReaderCashFlow:
        return XMLReaderCashFlow()