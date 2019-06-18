from reader.IReaderController import IReaderController

from model.BankStatement import BankStatement

import xml.etree.ElementTree as ET

class XMLReaderController(IReaderController):
    def read(self, factory, inputFilename='', file=None) -> BankStatement:
        data = ''

        if file is not None:
            data = readFile(file)
        else:
            with open(inputFilename, 'r', encoding='iso-8859-1') as inputFile:
                data = readFile(inputFile)
            
        tree = ET.fromstring(data)

        bsReader = factory.createReaderBankStatement()
        bs = bsReader.read(factory, tree)
        return bs

    def readFile(self, file):
        data = file.read()
        data = data[data.find('<OFX>'):]
        return data