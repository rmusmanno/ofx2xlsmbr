import abc

from model.BankStatement import BankStatement

class IWriterBankStatement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, bankStatement: BankStatement, factory, output):
        pass