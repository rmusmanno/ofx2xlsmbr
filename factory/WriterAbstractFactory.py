import abc

from writer.IWriterBankStatement import IWriterBankStatement
from writer.IWriterCashFlow import IWriterCashFlow

class WriterAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createWriterBankStatement(self) -> IWriterBankStatement:
        pass

    @abc.abstractmethod
    def createWriterCashFlow(self) -> IWriterCashFlow:
        pass