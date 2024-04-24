class Bank:
    def __init__(self,name) -> None:
        self.accounts = []
        self.admins = []
        self.bank_balance = 0
        self.bank_loan = 0

    def add_admin(self,admin):
        self.admins.append(admin)

    def add_user(self,user):
        self.accounts.append(user)