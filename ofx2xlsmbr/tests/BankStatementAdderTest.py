from ..utils.BankStatementAdder import BankStatementAdder

from ..model.BankStatement import BankStatement
from ..model.CashFlow import CashFlow, CashFlowType

import datetime
import logging

logger = logging.getLogger(__name__)

def bankStatementAdderTest():
    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now().date()),
                CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now().date()),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0, datetime.datetime.now().date()),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0, datetime.datetime.now().date())]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0, datetime.datetime.now().date())]

    bs = BankStatement(inflow, outflow)

    inflow2 = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0, datetime.datetime.now().date()),
                CashFlow('credit 2', CashFlowType.CREDIT, 2000.0, datetime.datetime.now().date())]

    bs2 = BankStatement(inflow2, outflow)

    adder = BankStatementAdder()
    bsResult = adder.add(bs, bs2)

    logger.info(bsResult)