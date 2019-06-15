from factory.OFXReaderFactory import OFXReaderFactory

import logging

logger = logging.getLogger(__name__)

def ofxReaderTest():
    factory = OFXReaderFactory()
    controller = factory.createReaderController()

    bs = controller.read(factory, './ofx/extrato_teste.ofx')
    logger.info(str(bs))