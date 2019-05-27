from .IReaderController import IReaderController

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

import datetime

class OFXReaderController(IReaderController):
    def read(self, factory, inputFilename) -> BankStatement:
        bs = BankStatement()

        with open(inputFilename, 'r', encoding='ISO-8859-1') as ofxFile:
            content = ofxFile.read()
            
            # TODO: resolver isto por regex
            begin = '<OFX>'
            end = '</OFX>'
            xml = begin + (content.split(begin)[1].split(end)[0]) + end
            print(xml)

        '''
        cs = CashFlow(name='cashflow 1',
                    flowType=CashFlowType.DEBIT,
                    value=-100.0,
                    date=datetime.datetime.now())

        bs.inflows.append(cs)
        '''
        
        return bs