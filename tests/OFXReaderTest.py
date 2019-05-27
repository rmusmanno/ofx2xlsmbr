from factory.OFXReaderFactory import OFXReaderFactory

def ofxReaderTest():
    factory = OFXReaderFactory()
    controller = factory.createReaderController()

    bs = controller.read(factory, './ofx/extrato_teste.ofx')
    print(str(bs))