from tests.CSVWriterTest import csvWriterControllerTest
from tests.OFXReaderTest import ofxReaderTest

from controller.AppController import AppController

import logging, sys

# TODO: passar isso para uma unidade de testes. Manter a main enxuta
def runTests():
    print('running tests')
    #ofxReaderTest()
    #csvWriterControllerTest()
    #csvFactoryTest()

def main():
    # logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

    #runTests()
    app = AppController()
    app.run()


if __name__ == "__main__":
    main()