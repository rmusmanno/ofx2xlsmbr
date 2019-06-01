from .IReaderController import IReaderController

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

import datetime

from ofxtools import OFXTree

class OFXReaderController(IReaderController):
    def read(self, factory, inputFilename) -> BankStatement:
        tree = OFXTree()
        tree.parse(inputFilename)
        convertedTree = tree.convert()

        bsReader = factory.createReaderBankStatement()
        bs = bsReader.read(factory, convertedTree)

        return bs