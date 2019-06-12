from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow

from writer.IWriterController import IWriterController

class XLSMWriterController(IWriterController):
    def write(self, data: BankStatement, factory, outputFilename):
        # create worksheet
        wb = Workbook()
        ws = wb.active

        formula = '"1,2,3,4,5,6,7"'

        # create data validation
        dv = DataValidation(type="list", formula1=formula, allow_blank=True)
        ws.add_data_validation(dv)

        writerBS = factory.createWriterBankStatement()
        writerBS.write(data, factory, [ws, dv])

        #dv.add(ws['A1'])

        wb.save(filename = outputFilename + '.xlsm')