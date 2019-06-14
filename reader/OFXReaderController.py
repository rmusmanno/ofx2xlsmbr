from .IReaderController import IReaderController

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

import datetime
from pytz import timezone
import pytz

import ofxtools
from ofxtools import OFXTree

class OFXReaderController(IReaderController):
    def read(self, factory, inputFilename) -> BankStatement:
        tree = OFXTree()
        tree.parse(inputFilename)

        # erros de compatibilidade
        self.treatBradescoException(tree)
        
        convertedTree = tree.convert()

        bsReader = factory.createReaderBankStatement()
        bs = bsReader.read(factory, convertedTree)

        return bs

    def treatBradescoException(self, tree):
        root = tree.getroot()
        dtServer = root.findall("SIGNONMSGSRSV1")[0].findall("SONRS")[0].findall("DTSERVER")[0]
        try:
            if (int(dtServer.text) == 0):
                unknownDateInThePast = datetime.datetime(1985, 10, 21, tzinfo=timezone('Brazil/East'))
                dtServer.text = unknownDateInThePast
        except ValueError:
            pass
            # se dtServer for um datetime, ele da erro na conversao para int
            # print('Correcting DTServer')