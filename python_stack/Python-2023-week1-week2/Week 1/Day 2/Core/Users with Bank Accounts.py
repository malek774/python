from bankaccout import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    def make_deposit(self,amount):
        self.account.deposit(amount)
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        print('--------------------------')
        print('User Informations :')
        print('--------------------------')
        print(f'Name : {self.name}')
        print('--------------------------')
        print(f'E-mail : {self.email}')
        print('--------------------------')
        self.account.display_account_info()
    

u1 = User('malek','malek@gmail.com')
u1.make_deposit(20)
u1.display_user_balance()