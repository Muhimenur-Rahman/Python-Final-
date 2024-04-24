class User:
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number =  name[:3]+'000'+'_'+account_type
        self.transactions = []
        self.loan_count = 0


    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f'Deposited : {amount}')

    def withdraw(self,amount):
            self.balance -= amount   
            self.transactions.append(f'Withdrawn : {amount}')

    def check_balance(self):
        print(f'\nAccount Balance : {self.balance}\n')
        
    def check_transactions(self):
        if(len(self.transactions) == 0):
            print('No Transaction History')
        else:
            for str in self.transactions:
                print(str)

    def take_loan(self,amount):
        flag = None
        if(self.loan_count <2):
            self.balance += amount
            self.loan_count += 1
            print(f'\n You have given loan of {amount} \n')
            self.transactions.append(f'Loan taken of {amount}')
            flag = True
        else:
            print('\n You Have taken 2 times Loan already. Bank can\'t give you any more loans \n')
            flag = False
        return flag

    def transfer_money(self,user,amount):
            user.balance += amount
            self.balance -= amount
            self.transactions.append(f'{amount} of money transferred to {user.name}')
            user.transactions.append(f'money {amount} has come from {self.name}')