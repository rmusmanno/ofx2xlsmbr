from .IReaderCashFlow import IReaderCashFlow
from model.CashFlow import CashFlow

class OFXReaderCashFlow(IReaderCashFlow):
    def read(self, factory, tree) -> CashFlow:
        cs = CashFlow()   
        print('read ofx CashFlow')
        return cs
