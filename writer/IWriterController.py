import abc

class IWriterController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, data, outputFilename):
        pass