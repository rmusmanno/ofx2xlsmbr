#from ofx2xlsmbr.tests.CSVWriterTest import csvWriterControllerTest
#from ofx2xlsmbr.tests.XLSWriterTest import xlsWriterControllerTest, xlsMultipleWriterControllerTest
#from ofx2xlsmbr.tests.OFXReaderTest import ofxReaderTest, ofxReaderTestCartaoBradesco, ofxReaderTestCartaoBradescoDuplo, ofxReaderTestCartaoBradesco2, ofxReaderTestFile, ofxMultipleReaderTestFile
#from ofx2xlsmbr.tests.XMLReaderTest import xmlReaderTestFile, xmlReaderTestFileCreditCard, ofxXmlReaderTestFile
#from ofx2xlsmbr.tests.XLSReaderTest import xlsReaderTestFile, xlsReaderTestFile2, xlsReaderTestFile3, xlsReaderTestFile_Origem, xlsMultipleReaderTestFile
from ofx2xlsmbr.tests.PDFReaderTest import pdfReaderTest
#from ofx2xlsmbr.tests.ProsperarCoreTest import prosperarCoreTest, prosperarCoreTestBBCartao, prosperarCoreTestInputDuploOfx, prosperarCoreTestReturnBS, prosperarCoreTestOFXAndXLS, prosperarCoreTestDuplicateEntry, prosperarCoreTestReceiveBS
#from ofx2xlsmbr.tests.BankStatementAdderTest import bankStatementAdderTest
#from ofx2xlsmbr.controller.AppController import AppController

#from ofx2xlsmbr.tests.BSWriterTest import BSWriterTest

import logging, sys
import unittest

logger = logging.getLogger(__name__)

# TODO: passar isso para uma unidade de testes. Manter a main enxuta
# FIXME: Alguns testes nao funcionam por mudanca de logica de negocio
def runTests():
    logger.info('running tests')
    #bankStatementAdderTest()
    #prosperarCoreTest()
    #prosperarCoreTestBBCartao()
    #prosperarCoreTestInputDuploOfx()
    #prosperarCoreTestReturnBS()
    #prosperarCoreTestOFXAndXLS()
    #prosperarCoreTestDuplicateEntry()
    #prosperarCoreTestReceiveBS()
    #ofxReaderTest()
    #ofxReaderTestCartaoBradesco()
    #ofxReaderTestCartaoBradescoDuplo()
    #ofxReaderTestCartaoBradesco2()
    #ofxReaderTestFile()
    #ofxMultipleReaderTestFile()
    #xmlReaderTestFile()
    #xmlReaderTestFileCreditCard()
    #ofxXmlReaderTestFile()
    #xlsReaderTestFile()
    #xlsReaderTestFile2()
    #xlsReaderTestFile3()
    #xlsReaderTestFile_Origem()
    #xlsMultipleReaderTestFile()
    #csvWriterControllerTest()
    #csvFactoryTest()
    #xlsWriterControllerTest()
    #xlsMultipleWriterControllerTest()
    pdfReaderTest()

    #suite = unittest.TestLoader().loadTestsFromTestCase(BSWriterTest)

    #unittest.TextTestRunner().run(suite)


def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    runTests()

    #app = AppController()
    #app.run()


if __name__ == "__main__":
    main()
