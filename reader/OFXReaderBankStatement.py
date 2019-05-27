from .IReaderBankStatement import IReaderBankStatement
from model.BankStatement import BankStatement

class OFXReaderBankStatement(IReaderBankStatement):
    def read(self, factory) -> BankStatement:
        print('read ofx BankStatement')