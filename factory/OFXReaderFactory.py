from .ReaderAbstractFactory import ReaderAbstractFactory

from reader.IReaderCashFlow import IReaderCashFlow
from reader.OFXReaderCashFlow import OFXReaderCashFlow

from reader.IReaderBankStatement import IReaderBankStatement
from reader.OFXReaderBankStatement import OFXReaderBankStatement

from reader.IReaderController import IReaderController
from reader.OFXReaderController import OFXReaderController

class OFXReaderFactory(ReaderAbstractFactory):
    def createReaderController(self) -> IReaderController:
        return OFXReaderController()

    def createReaderBankStatement(self) -> IReaderBankStatement:
        return OFXReaderBankStatement()
    
    def createReaderCashFlow(self) -> IReaderCashFlow:
        return OFXReaderCashFlow()