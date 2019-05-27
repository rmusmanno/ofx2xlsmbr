import abc

from reader.IReaderBankStatement import IReaderBankStatement
from reader.IReaderCashFlow import IReaderCashFlow

class ReaderAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createReaderBankStatement(self) -> IReaderBankStatement:
        pass

    @abc.abstractmethod
    def createReaderCashFlow(self) -> IReaderCashFlow:
        pass