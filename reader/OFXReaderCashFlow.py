from .IReaderCashFlow import IReaderCashFlow
from model.CashFlow import CashFlow

class OFXReaderCashFlow(IReaderCashFlow):
    def read(self, factory) -> CashFlow:        
        print('read ofx CashFlow')
