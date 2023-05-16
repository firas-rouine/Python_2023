class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-5
        else:
            self.balance=self.balance-amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        
    def yield_interest(self):
        self.balance=self.balance*self.int_rate
        return self
    @classmethod
    def instanceBanck(cls):
        cls.account_1=BankAccount(0.01,800)
        cls.account_2=BankAccount(0.2,1200)
        cls.account_1.deposit(50).deposit(60).deposit(80).withdraw(200).display_account_info()
        cls.account_2.deposit(750).deposit(250).withdraw(150).withdraw(500).withdraw(200).withdraw(50).yield_interest().display_account_info()
BankAccount.instanceBanck()



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print("user:",self.name,",","Balance:",self.account.balance)
        return self
    
user_1=User("firas","rouine.firas@gmail.com")
user_1.make_deposit(100).make_withdraw(10).display_user_balance()
