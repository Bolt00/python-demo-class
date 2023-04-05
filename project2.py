# A SIMPLE BANKING SYSTEM TO CREATE BANK ACCOUNT
#  AND TO BE ABLE TO TRANSFER, DEPOSIT AND WITHDRAW

import random


class RandomNumbers:
    def __init__(self):
        self.random1 = random.randint(1730927832, 9563029472)
        self.random2 = random.randint(300, 5000)


class Withdrawal:
    def __init__(self):
        self.withdraw = ['Savings', 'Current']


class Deposit:
    def __init__(self):
        self.deposit = ['Ghost Bank',
                        'United Bank for Africa (UBA)', 'Zenith Bank']


class Transfer:
    def __init__(self):
        self.transfer = ['Ghost Bank',
                         'United Bank for Africa (UBA)', 'Zenith Bank']


class Customer(RandomNumbers, Withdrawal, Deposit, Transfer):
    def __init__(self):
        RandomNumbers.__init__(self)
        Withdrawal.__init__(self)
        Deposit.__init__(self)
        Transfer.__init__(self)

    def Transaction(self):
        print('WELCOME TO GHOST BANK')

        first_name = input('What is your first name? ').capitalize()
        last_name = input('What is your last name? ').capitalize()
        print(f'Hello {first_name} {last_name}, this is your account number {self.random1}. choose the department you want to perform an operation by entering the number.')
        print('Enter 1 for withdrawal \n Enter 2 for Deposit \n Enter 3 for transfer')
        try:
            operation = int(
                input('Enter 1 for withdrawal \n Enter 2 for Deposit \n Enter 3 for transfer: '))
            if operation == 1:
                print('Saving or current? \n Enter 1 for savings \n Enter 2 for current')
                try:
                    savings_or_current = int(
                        input('Enter 1 for savings \n Enter 2 for current: '))
                    if savings_or_current == 1 or savings_or_current == 2:
                        try:
                            withdrawal = int(
                                input('How much do you want to withdraw? '))
                            if withdrawal != '':
                                print(
                                    f'Hello {first_name} {last_name} you have successfully withdrawn ${withdrawal}, please take your cash.')
                            else:
                                print('Withdrawals amount cannot be empty.')
                        except:
                            print('Withdrawal amount can only be numbers.')
                    else:
                        print('Incorrect selection')

                except:
                    print('Selection must be numbers only')

            elif operation == 2:
                print(self.deposit)
                print(
                    'Enter 1 for Ghost Bank \n Enter 2 for United Bank for Africa (UBA) \n Enter 3 for Zenith Bank')
                try:
                    choose_bank = int(input(
                        'Enter 1 for Ghost Bank \n Enter 2 for United Bank for Africa (UBA) \n Enter 3 for Zenith Bank: '))
                    if choose_bank == 1:
                        acct_name = input(
                            'Enter the account name you want to deposit into: ')
                        acct_number = int(
                            input('Enter the account number you want to deposit into: '))
                        amount = int(
                            input(f'Enter the amount you want to send to {acct_name}'))
                        if amount != '':
                            print(
                                f'You have successfully deposited ${amount} into \n account name: {acct_name} \n accont number: {acct_number} \n bank name: Ghost Bank')
                        else:
                            print('Deposit amount cannot be empty.')

                    elif choose_bank == 2:
                        acct_name1 = input(
                            'Enter the account name you want to deposit into: ')
                        acct_number1 = int(
                            input('Enter the account number you want to deposit into: '))
                        amount1 = int(
                            input(f'Enter the amount you want to send to {acct_name1}'))
                        if amount1 != '':
                            print(
                                f'You have successfully deposited ${amount1} into \n account name: {acct_name1} \n accont number: {acct_number1} \n bank name: UBA Bank')
                        else:
                            print('Deposit amount cannot be empty.')

                    elif choose_bank == 3:
                        acct_name2 = input(
                            'Enter the account name you want to deposit into: ')
                        acct_number2 = int(
                            input('Enter the account number you want to deposit into: '))
                        amount2 = int(
                            input(f'Enter the amount you want to send to {acct_name2}'))
                        if amount2 != '':
                            print(
                                f'You have successfully deposited ${amount2} into \n account name: {acct_name2} \n accont number: {acct_number2} \n bank name: Zenith Bank')
                        else:
                            print('Deposit amount cannot be empty.')
                    else:
                        print('Invalid selection.')
                except:
                    print('Selection must be numbers only.')

            elif operation == 3:
                print(self.transfer)
                print(
                    'Enter 1 for Ghost Bank \n Enter 2 for United Bank for Africa (UBA) \n Enter 3 for Zenith Bank')
                try:
                    banking = int(input(
                        'Enter 1 for Ghost Bank \n Enter 2 for UBA Bank \n Enter 3 for Zenith Bank'))
                    if banking == 1:
                        try:
                            print(
                                'Saving or Current? Enter 1 for Current \n Enter 2 for Savings')
                            savings_or_current1 = int(
                                input('Saving or Current? Enter 1 for Current \n Enter 2 for Savings'))
                            if savings_or_current1 == 1 or savings_or_current1 == 2:
                                enter_acct_name = input(
                                    'Enter the account name you want to transfer to: ').capitalize()
                                enter_account_number = int(
                                    input('Enter account number you want to send to: '))
                                enter_amount = int(
                                    input(f'Enter the amount you want to send to {enter_acct_name}: '))
                                if enter_amount != '':
                                    print(
                                        f'Do you want to send ${enter_amount} to {enter_account_number}? \n Enter Yes to send \n Enter No to cancel.')
                                    verify = input(
                                        'Enter Yes to send, Enter No to cancel: ').capitalize()
                                    if verify == 'Yes':
                                        print(
                                            f'You have successfully transfered ${enter_amount} to \n account name: {enter_acct_name} \n account number: {enter_account_number} \n Bank: Ghost Bank')
                                    elif verify == 'No':
                                        print('Transaction cancelled.')
                                    else:
                                        print('Invalid option')
                                else:
                                    print('You cannot transfer empty amount.')
                            else:
                                print('Invalid selection')
                        except:
                            print('Invalid selection.')

                    elif banking == 2:
                        try:
                            print(
                                'Saving or Current? Enter 1 for Current \n Enter 2 for Savings')
                            savings_or_current0 = int(
                                input('Saving or Current? Enter 1 for Current \n Enter 2 for Savings'))
                            if savings_or_current0 == 1 or savings_or_current0 == 2:
                                enter_acct_name0 = input(
                                    'Enter the account name you want to transfer to: ').capitalize()
                                enter_account_number0 = int(
                                    input('Enter account number you want to send to: '))
                                enter_amount0 = int(
                                    input(f'Enter the amount you want to send to {enter_acct_name0}: '))
                                if enter_amount0 != '':
                                    print(
                                        f'Do you want to send ${enter_amount0} to {enter_account_number0}? \n Enter Yes to send \n Enter No to cancel.')
                                    verify0 = input(
                                        'Enter Yes to send, Enter No to cancel: ').capitalize()
                                    if verify0 == 'Yes':
                                        print(
                                            f'You have successfully transfered ${enter_amount0} to \n account name: {enter_acct_name0} \n account number: {enter_account_number0} \n Bank: UBA Bank')
                                    elif verify0 == 'No':
                                        print('Transaction cancelled.')
                                    else:
                                        print('Invalid option')
                                else:
                                    print('You cannot transfer empty amount.')
                            else:
                                print('Invalid selection')
                        except:
                            print('Invalid selection.')

                    elif banking == 3:
                        try:
                            print(
                                'Saving or Current? Enter 1 for Current \n Enter 2 for Savings')
                            savings_or_current5 = int(
                                input('Saving or Current? Enter 1 for Current \n Enter 2 for Savings'))
                            if savings_or_current5 == 1 or savings_or_current5 == 2:
                                enter_acct_name5 = input(
                                    'Enter the account name you want to transfer to: ').capitalize()
                                enter_account_number5 = int(
                                    input('Enter account number you want to send to: '))
                                enter_amount5 = int(
                                    input(f'Enter the amount you want to send to {enter_acct_name5}: '))
                                if enter_amount5 != '':
                                    print(
                                        f'Do you want to send ${enter_amount5} to {enter_account_number5}? \n Enter Yes to send \n Enter No to cancel.')
                                    verify0 = input(
                                        'Enter Yes to send, Enter No to cancel: ').capitalize()
                                    if verify0 == 'Yes':
                                        print(
                                            f'You have successfully transfered ${enter_amount5} to \n account name: {enter_acct_name5} \n account number: {enter_account_number5} \n Bank: Zenith Bank')
                                    elif verify0 == 'No':
                                        print('Transaction cancelled.')
                                    else:
                                        print('Invalid option')
                                else:
                                    print('You cannot transfer empty amount.')
                            else:
                                print('Invalid selection')
                        except:
                            print('Invalid selection.')

                    else:
                        print('Bank doesn\'t exist.')
                except:
                    print('Bank selection must be numbers only')

        except:
            print('Selection must be numbers only')


obj = Customer()
obj.Transaction()
