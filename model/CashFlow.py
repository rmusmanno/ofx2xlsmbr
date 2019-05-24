from enum import Enum

class CashFlowType(Enum):
    DEBIT = 1
    CREDIT = 2

class CashFlow:
    def __init__(self, 
                flowType: CashFlowType = CashFlowType.DEBIT, 
                value: float = 0.0):
        self.flowType = flowType
        self.value = value

    def __repr__(self):
        return 'CashFlow:\n\tType: {}\n\tValue: {}'.format(self.flowType.name, self.value)