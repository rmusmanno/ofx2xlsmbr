from ..factory.XLSMWriterFactory import XLSMWriterFactory

from ..model.BankStatement import BankStatement
from ..model.CashFlow import CashFlow, CashFlowType
from ..model.Origin import Origin, AccountType

from collections import namedtuple

import datetime
import logging

logger = logging.getLogger(__name__)

def xlsWriterControllerTest():
    factory = XLSMWriterFactory()

    Account = namedtuple('Account', 'acctid')
    account = Account(acctid = '1112213141')
    origin_credit = Origin(account)
    origin_credit.account_type = AccountType.CREDITCARD

    origin_debit = Origin(account)
    origin_debit.account_type = AccountType.BANKACCOUNT

    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now(), origin=origin_debit),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0, origin=origin_debit),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0, origin=origin_credit)]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0, origin=origin_credit)]

    bs = BankStatement()
    bs.inflows = inflow
    bs.outflows = outflow

    writerController = factory.createWriterController()
    writerController.write([bs], factory, 'test')

def xlsMultipleWriterControllerTest():
    factory = XLSMWriterFactory()

    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now()),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0)]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

    inflow2 = [CashFlow('credit 2', CashFlowType.CREDIT, 2000.0)]

    bs = BankStatement(inflow, outflow)
    bs2 = BankStatement(inflow2, outflow)

    writerController = factory.createWriterController()
    writerController.write([bs, bs2], factory, 'test')