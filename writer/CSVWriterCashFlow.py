from .IWriterCashFlow import IWriterCashFlow
from model.CashFlow import CashFlow

class CSVWriterCashFlow(IWriterCashFlow):
    def write(self, cashFlow: CashFlow, csvOutput = ['']):        
        csvOutput[0] += str(cashFlow)