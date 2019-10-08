from ..IReaderCashFlow import IReaderCashFlow
from ofx2xlsmbr.model.CashFlow import CashFlow
from ofx2xlsmbr.model.Origin import Origin

import logging

logger = logging.getLogger(__name__)


class PDFReaderCashFlow(IReaderCashFlow):
    def read(self, factory, ofx) -> CashFlow:
        cs = CashFlow()

        result = ofx

        cs.date = result[0]
        cs.name = result[1]
        cs.value = result[2]

        if len(result) > 3:
            last_digits = result[3]
            cs.origin = Origin(type='CREDITCARD', account=last_digits)

        return cs
