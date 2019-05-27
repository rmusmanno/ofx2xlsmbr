import csv

from .IWriterController import IWriterController

class CSVWriterController(IWriterController):
    def write(self, data, outputFilename):
        # write data to file
        pass