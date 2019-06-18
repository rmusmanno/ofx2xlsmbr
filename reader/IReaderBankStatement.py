import abc

from model.BankStatement import BankStatement

class IReaderBankStatement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, factory, ofx) -> BankStatement:
        pass