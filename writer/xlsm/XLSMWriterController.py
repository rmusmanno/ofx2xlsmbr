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

        formula = '"Profissão,Habitação,Transporte,Dependentes,Saúde,Bem-estar,Outros"'

        # create data validation
        dv = DataValidation(type="list", formula1=formula, allow_blank=True)
        ws.add_data_validation(dv)

        writerBS = factory.createWriterBankStatement()
        writerBS.write(data, factory, [ws, dv])

        wb.save(filename = outputFilename + '.xlsm')