from factory.OFXReaderFactory import OFXReaderFactory
from factory.CSVWriterFactory import CSVWriterFactory

class AppController():
    inputFilename = './files/input.ofx'

    def run(self):
        #ler o caminho do arquivo e verificar se ele existe
        inputFilename = self.inputFilename
        if (inputFilename is None or inputFilename == ''):
            print('No file specified. Use parameter -e INPUT=<filename>')
            return

        #chamar o leitor ofx
        print('Reading file: ' + inputFilename)
        factoryOFX = OFXReaderFactory()
        readerController = factoryOFX.createReaderController()
        bs = readerController.read(factoryOFX, inputFilename)

        #chamar o escritor csv
        outputFilename = './files/output'
        print('Writing to file: ' + outputFilename)
        factoryCSV = CSVWriterFactory()
        writerController = factoryCSV.createWriterController()
        writerController.write(bs, factoryCSV, outputFilename)