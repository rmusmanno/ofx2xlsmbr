from enum import Enum

from .IReaderBankStatement import IReaderBankStatement
from ofx2xlsmbr.model.BankStatement import BankStatement

from decimal import Decimal

import logging

logger = logging.getLogger(__name__)

class OFXReaderBankStatement(IReaderBankStatement):
    def read(self, factory, ofx, options=None):
        signalMultiplier = 1
        if (options):
            if (options['creditcard'] == True):
                signalMultiplier = -1

        stmts = ofx.statements

        csReader = factory.createReaderCashFlow()

        bankStmts = []
        
        # btmts -> bs
        for stmt in stmts:
            bs = BankStatement()
            
            
            origin_dict = {
                'institution_number': institution_number,
                'branch_number': branch_id,
                'account_number': account_id,
                'type': AccountType
            }

            

            txs = stmt.transactions

            for tx in txs:
                cs = csReader.read(factory, tx)
                cs.value = Decimal(cs.value)
                cs.value *= signalMultiplier
                if (cs.value >= Decimal(0.0)):
                    bs.inflows.append(cs)
                else:
                    bs.outflows.append(cs)
                
                cs.origin = origin_dict

            bankStmts.append(bs)

        return bankStmts