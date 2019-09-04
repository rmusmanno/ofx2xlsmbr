from ..factory.BSWriterFactory import BSWriterFactory

from ..model.BankStatement import BankStatement
from ..model.CashFlow import CashFlow, CashFlowType
from ..model.Origin import Origin, AccountType

from collections import namedtuple
import datetime
import logging
import unittest
import sys

logger = logging.getLogger(__name__)


class BSWriterTest(unittest.TestCase):

    def test_bsWriterController(self):
        factory = BSWriterFactory()
        Account = namedtuple('Account',['acctid','bankid','branchid'])
        account = Account(acctid='132454',bankid='458',branchid='4567')
        outflow = [
            CashFlow(
                'debit 1',
                CashFlowType.DEBIT,
                -100.0,
                datetime.datetime.now(),
                Origin(
                    account
                )
            ),
            CashFlow(
                'debit 2', 
                CashFlowType.DEBIT,
                -127.0,
                datetime.datetime.now(),
                Origin(
                    account
                )
            ),
            CashFlow(
                'credit 1', 
                CashFlowType.CREDIT,
                -42.0
            )
        ]

        inflow = [CashFlow('credit 1', CashFlowType.CREDIT, 1000.0)]

        bs = BankStatement()
        bs.inflows = inflow
        bs.outflows = outflow

        writerController = factory.createWriterController()
        bstmts = writerController.write([bs], factory)
        logger.info(bstmts)


    def test_bsMultipleWriterController(self):
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
        bstmts = writerController.write([bs, bs2], factory)
        logger.info(bstmts)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    unittest.main()
