from .IReaderController import IReaderController

from model.BankStatement import BankStatement
from model.CashFlow import CashFlow, CashFlowType

from factory.XMLReaderFactory import XMLReaderFactory

import datetime
from pytz import timezone
import pytz

import logging

logger = logging.getLogger(__name__)

import ofxtools
from ofxtools import OFXTree

class OFXReaderController(IReaderController):
    def read(self, factory, inputFilename) -> BankStatement:
        try:
            tree = OFXTree()
            tree.parse(inputFilename)

            # erros de compatibilidade
            self.treatBradescoException(tree)
            
            convertedTree = tree.convert()

            bsReader = factory.createReaderBankStatement()
            bs = bsReader.read(factory, convertedTree)

            return bs
        except IndexError:
            # ofx nao consegue ler versao 220. Ler como XML
            xmlFactory = XMLReaderFactory()
            xmlReader = xmlFactory.createReaderController()
            return xmlReader.read(xmlFactory, inputFilename)

    # Estas duas proximas funcoes trazem desequilibrio ao Universo
    def treatBancoDoBrasilException(self, inputFilename):
        # ler ofx do banco do brasil como XML, ignorando o header dele.
        pass

    def treatBradescoException(self, tree):
        root = tree.getroot()
        dtServer = root.findall("SIGNONMSGSRSV1")[0].findall("SONRS")[0].findall("DTSERVER")[0]
        try:
            if (int(dtServer.text) == 0):
                unknownDateInThePast = datetime.datetime(1985, 10, 21, tzinfo=timezone('Brazil/East'))
                dtServer.text = unknownDateInThePast
        except ValueError:
            pass
            # se dtServer for um datetime, ele da erro na conversao para int
            # logger.info('Correcting DTServer')