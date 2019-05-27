import abc

from model.BankStatement import BankStatement

class IWriterController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, data: BankStatement, factory, outputFilename):
        pass