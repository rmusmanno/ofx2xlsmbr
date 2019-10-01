from ..factory.PDFReaderFactory import PDFReaderFactory
from ..reader.pdf.PDFReaderController import PDFReaderController

import logging

logger = logging.getLogger(__name__)

def pdfReaderTest():
    factory = PDFReaderFactory()
    controller = factory.createReaderController()
    
    with open('./ofx2xlsmbr/ofx/STARFISH 2019.pdf', 'rb') as inputFile:
        bs = controller.read(factory, files=[inputFile])
        logger.info(str(bs))