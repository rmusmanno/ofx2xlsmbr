from ..factory.XMLReaderFactory import XMLReaderFactory
from ..factory.OFXReaderFactory import OFXReaderFactory

import logging

logger = logging.getLogger(__name__)

def xmlReaderTestFile():
    factory = XMLReaderFactory()
    controller = factory.createReaderController()

    # este arquivo precisa ser criado  antes de testar
    with open('./ofx2xlsmbr/ofx/input_bancodobrasil.ofx', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))

def ofxXmlReaderTestFile():
    factory = OFXReaderFactory()
    controller = factory.createReaderController()

    # este arquivo precisa ser criado  antes de testar
    with open('./ofx2xlsmbr/ofx/input_bancodobrasil.ofx', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))