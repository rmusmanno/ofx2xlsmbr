import abc

from model.CashFlow import CashFlow

class IWriterCashFlow(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, cashFlow: CashFlow):
        pass