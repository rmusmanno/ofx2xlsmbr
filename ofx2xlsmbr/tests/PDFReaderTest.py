from ..factory.PDFReaderFactory import PDFReaderFactory
from ..reader.pdf.PDFReaderController import PDFReaderController

import logging

logger = logging.getLogger(__name__)

def pdfReaderTest():
    factory = PDFReaderFactory()
    controller = factory.createReaderController()
    
    with open('./ofx2xlsmbr/ofx/cartao itau.pdf', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))

        totalCount = 0
        for stmt in bs:
                totalCount += len(stmt.inflows) + len(stmt.outflows)
        logger.info('Total cashflows: ' + str(totalCount))