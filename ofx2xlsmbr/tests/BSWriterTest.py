from ..factory.BSWriterFactory import BSWriterFactory

from ..model.BankStatement import BankStatement
from ..model.CashFlow import CashFlow, CashFlowType

import datetime
import logging

logger = logging.getLogger(__name__)

def bsWriterControllerTest():
    factory = BSWriterFactory()

    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now()),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0)]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

    bs = BankStatement()
    bs.inflows = inflow
    bs.outflows = outflow

    writerController = factory.createWriterController()
    bstmtsJson = writerController.write([bs], factory)
    logger.info(bstmtsJson)

def bsMultipleWriterControllerTest():
    factory = BSWriterFactory()

    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now()),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0)]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

    inflow2 = [CashFlow('credit 2', CashFlowType.CREDIT, 2000.0)]

    bs = BankStatement()
    bs.inflows = inflow
    bs.outflows = outflow
    bs2 = BankStatement()
    bs2.inflows = inflow2
    bs2.outflows = outflow

    writerController = factory.createWriterController()
    bstmtsJson = writerController.write([bs], factory)
    logger.info(bstmtsJson)