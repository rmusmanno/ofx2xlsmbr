from ..factory.XLSMWriterFactory import XLSMWriterFactory

from ..model.BankStatement import BankStatement
from ..model.CashFlow import CashFlow, CashFlowType

import datetime
import logging

logger = logging.getLogger(__name__)

def xlsWriterControllerTest():
    factory = XLSMWriterFactory()

    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now()),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0)]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

    bs = BankStatement(inflow, outflow)

    writerController = factory.createWriterController()
    writerController.write(bs, factory, 'test')