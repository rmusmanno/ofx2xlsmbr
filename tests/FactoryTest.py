from factory.WriterAbstractFactory import WriterAbstractFactory
from factory.CSVWriterFactory import CSVWriterFactory

from writer.IWriterCashFlow import IWriterCashFlow
from writer.CSVWriterCashFlow import CSVWriterCashFlow

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

import datetime

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

    # print(str(bs))

    outputBS = ['']

    writerBS = factory.createWriterBankStatement()
    writerBS.write(bs, outputBS)

    print(outputBS[0])
    
    outputCS = ['']

    writerCS = factory.createWriterCashFlow()
    writerCS.write(inflow[0], outputCS)

    print(outputCS[0])