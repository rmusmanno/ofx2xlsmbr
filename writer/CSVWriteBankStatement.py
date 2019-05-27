from .IWriterBankStatement import IWriterBankStatement
from model.BankStatement import BankStatement

class CSVWriterBankStatement(IWriterBankStatement):
    def write(self, bankStatement: BankStatement, csvOutput = ['']):
        csvOutput[0] += str(bankStatement)