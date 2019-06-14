from reader.IReaderController import IReaderController

from model.BankStatement import BankStatement

import xml.etree.ElementTree as ET

class XMLReaderController(IReaderController):
    def read(self, factory, inputFilename) -> BankStatement:
        with open(inputFilename, 'r', encoding='iso-8859-1') as file:
            data = file.read()
            data = data[data.find('<OFX>'):]
            
            tree = ET.fromstring(data)

            bsReader = factory.createReaderBankStatement()
            bs = bsReader.read(factory, tree)
        return bs