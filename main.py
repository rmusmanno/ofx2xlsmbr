#from ofx2xlsmbr.tests.CSVWriterTest import csvWriterControllerTest
#from ofx2xlsmbr.tests.XLSWriterTest import xlsWriterControllerTest, xlsMultipleWriterControllerTest
#from ofx2xlsmbr.tests.OFXReaderTest import ofxReaderTest, ofxReaderTestFile, ofxMultipleReaderTestFile
#from ofx2xlsmbr.tests.XMLReaderTest import xmlReaderTestFile
#from ofx2xlsmbr.tests.ProsperarCoreTest import prosperarCoreTest
#from ofx2xlsmbr.controller.AppController import AppController

import logging, sys

logger = logging.getLogger(__name__)

# TODO: passar isso para uma unidade de testes. Manter a main enxuta
def runTests():
    logger.info('running tests')
    #prosperarCoreTest()
    #ofxReaderTest()
    #ofxReaderTestFile()
    #ofxMultipleReaderTestFile()
    #xmlReaderTestFile()
    #csvWriterControllerTest()
    #csvFactoryTest()
    #xlsWriterControllerTest()
    #xlsMultipleWriterControllerTest()

def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    runTests()
    #app = AppController()
    #app.run()


if __name__ == "__main__":
    main()