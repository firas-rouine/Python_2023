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