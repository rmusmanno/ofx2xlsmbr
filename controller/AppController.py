from factory.OFXReaderFactory import OFXReaderFactory

from factory.CSVWriterFactory import CSVWriterFactory
from factory.XLSMWriterFactory import XLSMWriterFactory

import logging

logger = logging.getLogger(__name__)

class AppController():
    inputFilename = './files/input.ofx'

    def run(self):
        #ler o caminho do arquivo e verificar se ele existe
        inputFilename = self.inputFilename
        if (inputFilename is None or inputFilename == ''):
            logger.info('No file specified. Use parameter -e INPUT=<filename>')
            return

        #chamar o leitor ofx
        logger.info('Reading file: ' + inputFilename)
        factoryOFX = OFXReaderFactory()
        readerController = factoryOFX.createReaderController()
        bs = readerController.read(factoryOFX, inputFilename)

        #chamar o escritor csv
        outputFilename = './files/output'
        logger.info('Writing to file: ' + outputFilename)
        #factory = CSVWriterFactory()
        factory = XLSMWriterFactory()
        writerController = factory.createWriterController()
        writerController.write(bs, factory, outputFilename)