from tests.CSVWriterTest import csvWriterControllerTest
from tests.OFXReaderTest import ofxReaderTest

# TODO: passar isso para uma unidade de testes. Manter a main enxuta
def runTests():
    print('running tests')
    ofxReaderTest()
    #csvWriterControllerTest()
    #csvFactoryTest()

def main():
    print('main called')
    runTests()

if __name__ == "__main__":
    main()