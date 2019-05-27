from .IReaderController import IReaderController

class OFXReaderController(IReaderController):
    def read(self, factory, inputFilename):
        print('ofx reader controller')