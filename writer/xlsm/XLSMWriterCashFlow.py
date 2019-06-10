from writer.IWriterCashFlow import IWriterCashFlow
from model.CashFlow import CashFlow

class XLSMWriterCashFlow(IWriterCashFlow):
    def write(self, cashFlow: CashFlow, factory, xlsmOutput):
        pass
        '''   
        csvOutput.append([
            str(cashFlow.date),
            cashFlow.name,
            cashFlow.value,
            cashFlow.flowType.name
        ])
        '''

    def writeHeader(self, xlsmOutput):
        pass
        '''
        csvOutput.append([
            'Date',
            'Name',
            'Value',
            'Type'
        ])
        '''