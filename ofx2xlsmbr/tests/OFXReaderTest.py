from ..factory.OFXReaderFactory import OFXReaderFactory
from ..reader.OFXReaderController import OFXReaderController

import logging

logger = logging.getLogger(__name__)

def ofxReaderTest():
    factory = OFXReaderFactory()
    controller = factory.createReaderController()

    bs = controller.read(factory, inputFilename='./ofx/extrato_teste.ofx')
    logger.info(str(bs))

def ofxReaderTestFile():
    factory = OFXReaderFactory()
    controller = factory.createReaderController()

    with open('./ofx2xlsmbr/ofx/extrato_teste.ofx', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))

    with open('./ofx2xlsmbr/ofx/extrato_teste.ofx', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))

def ofxMultipleReaderTestFile():
    factory = OFXReaderFactory()
    controller = factory.createReaderController()

    with open('./ofx2xlsmbr/ofx/extrato_teste.ofx', 'rb') as inputFile:
        with open('./ofx2xlsmbr/ofx/input.ofx', 'rb') as inputFile2:
            bs = controller.read(factory, files=[inputFile, inputFile2])
            logger.info(str(bs))