from writer.IWriterCashFlow import IWriterCashFlow
from model.CashFlow import CashFlow

class XLSMWriterCashFlow(IWriterCashFlow):
    def write(self, cashFlow: CashFlow, factory, xlsmOutput):
        ws = xlsmOutput[0]
        dv = xlsmOutput[1]
        row = xlsmOutput[2]

        cashFlowOutput = [
            str(cashFlow.date),
            cashFlow.name,
            cashFlow.value,
            cashFlow.flowType.name
        ]

        ws.append(cashFlowOutput)

        cell = ws.cell(column=len(cashFlowOutput)+1, row=row)
        dv.add(cell)

    def writeHeader(self, xlsmOutput):
        headers = [
            'Date',
            'Name',
            'Value',
            'Type',
            'Category'
        ]

        ws = xlsmOutput[0]

        for index, header in enumerate(headers):
            ws.cell(column=index+1, row=1, value="{}".format(header))