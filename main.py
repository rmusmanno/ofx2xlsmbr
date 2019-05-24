from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

outflow = [CashFlow(CashFlowType.DEBIT, -100.0),
            CashFlow(CashFlowType.DEBIT, -127.0),
            CashFlow(CashFlowType.CREDIT, -42.0)]

inflow = [CashFlow(CashFlowType.CREDIT, 1000.0)]

bs = BankStatement(inflow, outflow)

print(str(bs))