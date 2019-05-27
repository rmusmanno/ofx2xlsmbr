from .IWriterBankStatement import IWriterBankStatement
from model.BankStatement import BankStatement

class CSVWriterBankStatement(IWriterBankStatement):
    def write(self, bankStatement: BankStatement):
        print('Write BankStatement to CSV')
        print(str(bankStatement))