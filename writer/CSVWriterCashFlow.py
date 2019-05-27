from .IWriterCashFlow import IWriterCashFlow
from model.CashFlow import CashFlow

class CSVWriterCashFlow(IWriterCashFlow):
    def write(self, cashFlow: CashFlow):
        print('Write CashFlow to CSV')
        print(str(cashFlow))