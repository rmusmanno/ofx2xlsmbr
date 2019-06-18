from ProsperarCore import ProsperarCore

import logging

logger = logging.getLogger(__name__)

def prosperarCoreTest():
    pc = ProsperarCore()

    with open('./ofx/extrato_teste.ofx', 'rb') as inputFile:
        outputStream = pc.run(inputFile)
        with open('./files/output.xlsm','wb') as out:
            out.write(outputStream.read())