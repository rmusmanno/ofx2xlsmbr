import abc

from model.CashFlow import CashFlow

class IReaderCashFlow(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, factory, tree) -> CashFlow:
        pass