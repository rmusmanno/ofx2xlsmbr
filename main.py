from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType
import datetime

# TODO: passar isso para uma unidade de testes. Manter a main enxuta
outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now()),
            CashFlow('debit 2', CashFlowType.DEBIT, -127.0),
            CashFlow('credit 1', CashFlowType.CREDIT, -42.0)]

inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

bs = BankStatement(inflow, outflow)

print(str(bs))