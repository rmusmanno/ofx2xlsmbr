from factory.CSVWriterFactory import CSVWriterFactory

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

import datetime
import logging

logger = logging.getLogger(__name__)

def csvWriterControllerTest():
    factory = CSVWriterFactory()

    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now()),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0)]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

    bs = BankStatement(inflow, outflow)

    writerController = factory.createWriterController()
    writerController.write(bs, factory, 'test')

def csvFactoryTest():
    factory = CSVWriterFactory()

    outflow = [CashFlow('debit 1', CashFlowType.DEBIT, -100.0, datetime.datetime.now()),
                CashFlow('debit 2', CashFlowType.DEBIT, -127.0),
                CashFlow('credit 1', CashFlowType.CREDIT, -42.0)]

    inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

    bs = BankStatement(inflow, outflow)

    # logger.info(str(bs))

    outputBS = ['']

    writerBS = factory.createWriterBankStatement()
    writerBS.write(bs, outputBS)

    logger.info(outputBS[0])
    
    outputCS = ['']

    writerCS = factory.createWriterCashFlow()
    writerCS.write(inflow[0], outputCS)

    logger.info(outputCS[0])