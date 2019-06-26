from ..factory.XLSReaderFactory import XLSReaderFactory
from ..reader.xls.XLSReaderController import XLSReaderController

import logging

logger = logging.getLogger(__name__)

def xlsReaderTestFile():
    factory = XLSReaderFactory()
    controller = factory.createReaderController()

    with open('./ofx2xlsmbr/ofx/test.xlsx', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))

    with open('./ofx2xlsmbr/ofx/test.xlsx', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))

def xlsMultipleReaderTestFile():
    factory = XLSReaderFactory()
    controller = factory.createReaderController()

    with open('./ofx2xlsmbr/ofx/test.xlsx', 'rb') as inputFile:
        with open('./ofx2xlsmbr/ofx/test.xlsx', 'rb') as inputFile1:
            bs = controller.read(factory, files=[inputFile, inputFile1])
            logger.info(str(bs))