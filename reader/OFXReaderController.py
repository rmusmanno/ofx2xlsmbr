from .IReaderController import IReaderController

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

import datetime

from ofxtools import OFXTree

class OFXReaderController(IReaderController):
    def read(self, factory, inputFilename) -> BankStatement:
        bs = BankStatement()

        tree = OFXTree()
        tree.parse(inputFilename)

        print(tree)

        '''
        with open(inputFilename, 'r', encoding='ISO-8859-1') as ofxFile:
            content = ofxFile.read()

        
            # TODO: resolver isto por regex
            begin = '<OFX>'
            end = '</OFX>'
            ofx = begin + (content.split(begin)[1].split(end)[0]) + end
            print(ofx)
        
        cs = CashFlow(name='cashflow 1',
                    flowType=CashFlowType.DEBIT,
                    value=-100.0,
                    date=datetime.datetime.now())

        bs.inflows.append(cs)
        '''

        return bs