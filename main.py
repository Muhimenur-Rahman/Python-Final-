from admin import Admin
from bank import Bank
from user import User

def main():
    #create a bank
    db = Bank('Dhaka Bank Limited')


                   

    while(True):
        print('\n\nOption 1 : User')
        print('Option 2 : Admin')
        print('Option 3 : Exit')
        option = int(input('Enter an Option : '))
        if(option == 1):
            print('\nOption 1 : Register as a user')
            print('Option 2 : Login as a user')
            opt = int(input('Enter an option : '))
            if(opt == 1):
                name = input('Enter Your Name : ')
                email = input('Enter Your email address : ')
                address = input('Enter Your address : ')
                account_type = input('Enter Your Account Type (Savings or Current) : ')
                user = User(name,email,address,account_type)
                db.add_user(user)
                print(f'\nWelcome {user.name}! Your account has been created\n')
                print(f'Your account Number is {user.account_number}\n')
            elif(opt == 2):
                name = input('Enter Your Name : ')
                account_type = input('Enter Your Account Type (Savings or Current) : ')
                is_user = False
                user = None
                for account in db.accounts:
                    if name == account.name and account_type == account.account_type:
                        print(f'\n Welcome {name} \n')
                        user = account
                        is_user = True
                if(is_user == True):
                   while(True):
                        print('\n\nOption 1 : Deposite Money')
                        print('Option 2 : Withdraw Money')
                        print('Option 3 : Check Balance')
                        print('Option 4 : See Transaction History')
                        print('Option 5 : Take Loan')
                        print('Option 6 : Transfer Money')
                        print('Option 7 : Exit')
                        op = int(input('Enter an Option : '))
                        if op ==1 :
                            amount = int(input('Enter Amount of money you want to deposit : '))
                            user.deposit(amount)
                            print(f'\n{amount} has been deposited into your account\n')
                            db.bank_balance += amount
                        elif op == 2:
                            is_bankrupt = False
                            for admin in db.admins:
                                if admin.bankrupt == True:
                                    is_bankrupt = True
                                    break
                            if(is_bankrupt == True):
                                print('Bank is Bankrupt')
                            else:
                                amount = int(input('Enter Amount of money you want to withdraw : '))
                                if(amount <= user.balance):
                                    user.withdraw(amount)
                                    print(f'\n {amount} has been withdrawn into your account \n')
                                    db.bank_balance -= amount
                                else:
                                    print('\n Withdrawal amount exceeded \n')
                        elif op == 3:
                            user.check_balance()
                        elif op == 4:
                            user.check_transactions()
                        elif op == 5:
                            loan_available = True
                            for admin in db.admins:
                                if admin.loan_feature == False:
                                    loan_available = False
                                    break
                            if(loan_available == True):
                                amount = int(input('Enter Amount of money you want to take loan : '))
                                loan_taken = None
                                if(amount <= db.bank_balance):
                                    loan_taken = user.take_loan(amount)
                                    if(loan_taken == True):
                                        db.bank_balance -= amount
                                        db.bank_loan += amount
                                else:
                                    print(f'\n Bank does not have enough loans of {amount} \n')

                            else:
                                print('\n Sorry Bank is not offering any Loans \n')

                        elif op == 6:
                            another_user_name = input('Enter account Name : ')
                            another_account_type = input('Enter account type : ')
                            another_user_exists = False
                            another_user = None
                            for account in db.accounts:
                                if another_user_name == account.name and another_account_type == account.account_type:
                                    another_user_exists = True
                                    another_user = account
                                    break
                            if(another_user_exists == True):
                                amount = int(input('Enter Amount of money you want to transfer : '))
                                if(amount <= user.balance):
                                    user.transfer_money(another_user,amount)
                                    print(f'\n Money Transferred to {another_user.name} \n')

                                else:
                                    print('\n You have not enough money to transfer \n')
                            else:
                                print(f'\n Account does not Exists with name : {another_user_name} with account type : {another_account_type}\n')
                        elif op == 7 :
                            break
                        else : 
                            print('\n Invalid Option Number \n')
                else:
                    print(f'\n No User found \n')

            else:
                print('\n Invalid Option Number! \n')

        elif(option == 2):
            print('\nOption 1 : Register as an admin')
            print('Option 2 : Login as an admin')
            opt = int(input('Enter an option : '))
            if(opt == 1):
                name = input('Enter Your Name : ')
                email = input('Enter Your Email : ')
                admin = Admin(name,email,db)
                db.add_admin(admin)
                print(f'\nWelcome {admin.name}! Your account as an admin has been created \n')
            elif(opt == 2):
                name = input('Enter Your Name : ')
                email = input('Enter Your Email Address : ')
                is_admin = False
                admin = None
                for ans in db.admins:
                    if name == ans.name and email == ans.email:
                        print(f'\n Welcome {name} \n')
                        admin = ans
                        is_admin = True
                if(is_admin) == True:
                    while(True):
                        print('\nOption 1 : Delete an User Account')
                        print('Option 2 : See all user account list')
                        print('Option 3 : Check Total Balance of Bank')
                        print('Option 4 : Check Total Loan Amount')
                        print('Option 5 : Disable loan feature')
                        print('Option 6 : Enable loan feature')
                        print('Option 7 : Declare Bankrupt')
                        print('Option 8 : Exit')
                        op = int(input('Enter an option : '))
                        if(op == 1):
                            name = input('Enter User Name : ')
                            account_type = input('Enter User Account Type (Savings or Current) : ')
                            is_user = False
                            user = None
                            for account in db.accounts:
                                if name == account.name and account_type == account.account_type:
                                    user = account
                                    is_user = True
                            if(is_user == True):
                                admin.delete_account(user)
                                print(f' \n User account with name {user.name} has been deleted \n')
                            else:
                                print(f'\n No User found \n')
                        elif(op == 2):
                            try:
                                admin.see_accounts()
                            except:
                                print('\n No users in the Bank \n')
                        elif(op == 3):
                            admin.total_bank_balance()
                        elif(op == 4):
                            admin.total_loan_amount()
                        elif(op == 5):
                            admin.loan_off()
                        elif(op == 6):
                            admin.loan_on()
                        elif(op == 7):
                            admin.declare_bankrupt()
                        elif(op == 8):
                           break
                        else:
                            print('Invalid Option')
                else:
                    print(f'\nNo admin found with name {name} and email address {email}\n')

            else:
                print('\nInvalid Option\n')
        elif(option == 3):
            break
        else:
            print('\nInvalid Option Number!\n')

if __name__ == '__main__':
    main()