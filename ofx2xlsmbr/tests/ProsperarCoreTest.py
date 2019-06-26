from ..ProsperarCore import ProsperarCore

import logging

logger = logging.getLogger(__name__)

def prosperarCoreTest():
    pc = ProsperarCore()

    with open('./ofx2xlsmbr/ofx/extrato_teste.ofx', 'rb') as inputFile:
        with open('./ofx2xlsmbr/ofx/input.ofx', 'rb') as inputFile2:
            outputStream = pc.run([inputFile, inputFile2])
            with open('./output.xlsm','wb') as out:
                out.write(outputStream)