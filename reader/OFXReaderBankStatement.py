from .IReaderBankStatement import IReaderBankStatement
from model.BankStatement import BankStatement

class OFXReaderBankStatement(IReaderBankStatement):
    def read(self, factory, tree) -> BankStatement:
        bs = BankStatement()
        
        csReader = factory.createReaderCashFlow()
        # TODO: ler bs de da ofxTree

        cs = csReader.read(factory, tree)

        return bs