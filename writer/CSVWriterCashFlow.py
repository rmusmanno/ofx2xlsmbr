from .IWriterCashFlow import IWriterCashFlow
from model.CashFlow import CashFlow

class CSVWriterCashFlow(IWriterCashFlow):
    def write(self, cashFlow: CashFlow, csvOutput = []):        
        csvOutput.append([
            str(cashFlow.date),
            cashFlow.name,
            cashFlow.value,
            cashFlow.flowType.name
        ])

    def writeHeader(self, csvOutput = []):
        csvOutput.append([
            'Date',
            'Name',
            'Value',
            'Type'
        ])
