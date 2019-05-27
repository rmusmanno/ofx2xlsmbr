import abc

class IReaderController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, factory):
        pass