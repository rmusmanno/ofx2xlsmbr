from factory.OFXReaderFactory import OFXReaderFactory
from reader.OFXReaderController import OFXReaderController

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

    with open('./ofx/extrato_teste.ofx', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))