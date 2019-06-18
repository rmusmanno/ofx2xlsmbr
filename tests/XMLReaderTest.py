from factory.XMLReaderFactory import XMLReaderFactory

import logging

logger = logging.getLogger(__name__)

def xmlReaderTestFile():
    factory = XMLReaderFactory()
    controller = factory.createReaderController()

    # este arquivo precisa ser criado  antes de testar
    with open('./ofx/input_bancodobrasil.ofx', 'rb') as inputFile:
        bs = controller.read(factory, file=inputFile)
        logger.info(str(bs))