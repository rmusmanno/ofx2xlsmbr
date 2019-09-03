from ..ProsperarCore import ProsperarCore

import logging
import datetime
from collections import OrderedDict
from decimal import Decimal

logger = logging.getLogger(__name__)

def prosperarCoreTest():
    pc = ProsperarCore()

    with open('./ofx2xlsmbr/ofx/extrato_teste.ofx', 'rb') as inputFile:
        with open('./ofx2xlsmbr/ofx/input.ofx', 'rb') as inputFile2:
            outputStream = pc.run([inputFile, inputFile2])
            with open('./output.xlsx','wb') as out:
                out.write(outputStream)

def prosperarCoreTestInputDuploOfx():
    pc = ProsperarCore()

    with open('./ofx2xlsmbr/ofx/Bradesco_03092019_073504.ofx', 'rb') as inputFile:
        outputStream = pc.run(files=[inputFile])
        with open('./output.xlsx','wb') as out:
            out.write(outputStream)

def prosperarCoreTestReturnBS():
    pc = ProsperarCore()

    with open('./ofx2xlsmbr/ofx/extrato_teste.ofx', 'rb') as inputFile:
        with open('./ofx2xlsmbr/ofx/input.ofx', 'rb') as inputFile2:
            bsStmts = pc.run([inputFile, inputFile2], True)
            logger.info(bsStmts)

def prosperarCoreTestDuplicateEntry():
    pc = ProsperarCore()

    with open('./ofx2xlsmbr/ofx/input_bancodobrasil.ofx', 'rb') as inputFile:
        with open('./ofx2xlsmbr/ofx/input_bancodobrasil.ofx', 'rb') as inputFile2:
            outputStream = pc.run([inputFile, inputFile2])
            with open('./output.xlsx','wb') as out:
                out.write(outputStream)

def prosperarCoreTestOFXAndXLS():
    pc = ProsperarCore()

    with open('./ofx2xlsmbr/ofx/extrato_teste.ofx', 'rb') as inputFile:
        with open('./ofx2xlsmbr/ofx/test.xlsx', 'rb') as inputFile2:
            outputStream = pc.run([inputFile, inputFile2])
            with open('./output.xlsx','wb') as out:
                out.write(outputStream)

def prosperarCoreTestReceiveBS():
    pc = ProsperarCore()

    bs = {'id': 1, 'name': 'Consolidado Teste', 'CFP': OrderedDict([('user', OrderedDict([('first_name', 'Admin'), ('last_name', 'Teste'), ('email', 'admin@admin.com')])), ('telephone', '+5521996157576')]), 'cashflows': [OrderedDict([('id', 4), ('name', 'Resgate Fundo BB'), ('date', datetime.date(2019, 6, 13)), ('amount', Decimal('800.00')), ('origin', None), ('description', OrderedDict([('name', 'Regate de Aporte')])), ('category', None)]), OrderedDict([('id', 64), ('name', 'Emiss\\xe3o de DOC D - 237 2510 11251698778 RAFAEL MARICATO M'), ('date', datetime.date(2019, 6, 13)), ('amount', Decimal('-400.00')), ('origin', None), ('description', OrderedDict([('name', 'Pagamento de Fatura de Fotografo')])), ('category', None)]), OrderedDict([('id', 60), ('name', 'Pagto Eletron Cobranca'), ('date', datetime.date(2019, 6, 12)), ('amount', Decimal('-16.90')), ('origin', None), ('description', None), ('category', None)]), OrderedDict([('id', 61), ('name', 'Cartao Visa Electron'), ('date', datetime.date(2019, 6, 12)), ('amount', Decimal('-22.74')), ('origin', None), ('description', None), ('category', None)]), OrderedDict([('id', 1), ('name', 'Ted-transf Elet Dispon Remet.finxi Solucoes em t.'), ('date', datetime.date(2019, 6, 11)), ('amount', Decimal('1704.55')), ('origin', None), ('description', None), ('category', None)]), OrderedDict([('id', 59), ('name', 'Cartao Visa Electron mc Donalds Sfr'), ('date', datetime.date(2019, 6, 11)), ('amount', Decimal('-25.50')), ('origin', None), ('description', None), ('category', None)]), OrderedDict([('id', 3), ('name', 'BB RF CP Autom\\xe1tico Mais'), ('date', datetime.date(2019, 6, 10)), ('amount', Decimal('12.00')), ('origin', None), ('description', None), ('category', None)]), OrderedDict([('id', 63), ('name', 'Tarifa Pacote de Servi\\xe7os - Cobran\\xe7a referente 10/06/2019'), ('date', datetime.date(2019, 6, 10)), ('amount', Decimal('-12.00')), ('origin', None), ('description', None), ('category', None)]), OrderedDict([('id', 2), ('name', 'BB RF CP Autom\\xe1tico Mais'), ('date', datetime.date(2019, 6, 3)), ('amount', Decimal('800.00')), ('origin', None), ('description', None), ('category', None)])]}

    pc.createXLSX(bs)