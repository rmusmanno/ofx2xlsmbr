import abc

class IWriter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, data, outputFilename):
        pass