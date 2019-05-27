import csv

from .IWriter import IWriter

class CSVWriter(IWriter):
    def write(self, data, outputFilename):
        # write data to file
        pass