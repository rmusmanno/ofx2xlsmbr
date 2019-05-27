from .IWriterBankStatement import IWriterBankStatement
from model.BankStatement import BankStatement

class CSVWriterBankStatement(IWriterBankStatement):
    def write(self, bankStatement: BankStatement, factory, csvOutput):
        writerCS = factory.createWriterCashFlow()

        writerCS.writeHeader(csvOutput)
        for cs in bankStatement.inflows:
            writerCS.write(cs, factory, csvOutput)
        for cs in bankStatement.outflows:
            writerCS.write(cs, factory, csvOutput)