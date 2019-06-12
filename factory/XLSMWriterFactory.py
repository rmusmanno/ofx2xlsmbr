from .WriterAbstractFactory import WriterAbstractFactory

from writer.IWriterCashFlow import IWriterCashFlow
from writer.IWriterBankStatement import IWriterBankStatement
from writer.IWriterController import IWriterController

from writer.xlsm.XLSMWriterCashFlow import XLSMWriterCashFlow
from writer.xlsm.XLSMWriterBankStatement import XLSMWriterBankStatement
from writer.xlsm.XLSMWriterController import XLSMWriterController

class XLSMWriterFactory(WriterAbstractFactory):
    def createWriterController(self) -> IWriterController:
        return XLSMWriterController()

    def createWriterBankStatement(self) -> IWriterBankStatement:
        return XLSMWriterBankStatement()
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return XLSMWriterCashFlow()