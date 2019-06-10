from writer.IWriterBankStatement import IWriterBankStatement
from model.BankStatement import BankStatement

class CSVWriterBankStatement(IWriterBankStatement):
    def write(self, bankStatement: BankStatement, factory, xlsmOutput):
        pass
        '''
        writerCS = factory.createWriterCashFlow()

        writerCS.writeHeader(csvOutput)
        for cs in bankStatement.inflows:
            writerCS.write(cs, factory, csvOutput)
        for cs in bankStatement.outflows:
            writerCS.write(cs, factory, csvOutput)
        '''