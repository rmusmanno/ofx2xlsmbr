from .IReaderBankStatement import IReaderBankStatement
from ofx2xlsmbr.model.BankStatement import BankStatement

class OFXReaderBankStatement(IReaderBankStatement):
    def read(self, factory, ofx) -> BankStatement:
        bs = BankStatement()
        stmts = ofx.statements
        
        # btmts -> bs
        txs = stmts[0].transactions

        csReader = factory.createReaderCashFlow()
        for tx in txs:
            cs = csReader.read(factory, tx)
            if (cs.value >= 0.0):
                bs.inflows.append(cs)
            else:
                bs.outflows.append(cs)

        return bs