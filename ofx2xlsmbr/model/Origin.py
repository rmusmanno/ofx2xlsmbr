from enum import Enum

class AccountType(Enum):
    BANKACCOUNT = 0
    CREDITCARD = 1

class Origin:

    def __init__(self, account):
        self.account_id = account.acctid

        if hasattr(account,'bankid'):
            self.institution_number = account.bankid
            self.account_type = AccountType.BANKACCOUNT
            self.branch_id = None
        else:
            self.institution_number = None
            self.account_type = AccountType.BANKACCOUNT
            self.branch_id = None            

    def __str__(self):
        return "Account:{} / Type: {}".format(self.account_id, self.account_type)

    def __eq__(self, other):
        return(
            self.account_id == other.account_id and
            self.institution_number == other.institution_number and
            self.account_type == other.account_type and
            self.branch_id == other.branch_id
        )