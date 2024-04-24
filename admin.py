class Admin:
    def __init__(self,name,email,bank) -> None:
        self.name = name
        self.email = email
        self.bank = bank
        self.loan_feature = True
        self.bankrupt = False

    def delete_account(self,user):
        self.bank.accounts.remove(user)

    def see_accounts(self):
        for user in self.bank.accounts:
            print(f'Account Name : {user.name} Account Balance : {user.balance} Account Id : {user.account_number}')

    def total_bank_balance(self):
        print(f'Bank Total Balance : {self.bank.bank_balance}')

    def total_loan_amount(self):
        print(f'Bank Total Loan : {self.bank.bank_loan}')

    def loan_on(self):
        self.loan_feature = True
        print('Bank is giving loan now!')
    
    def loan_off(self):
        self.loan_feature = False
        print('Bank is not giving loan now!')

    def declare_bankrupt(self):
        self.bankrupt = True
        print('Bank is now Bankrupt')