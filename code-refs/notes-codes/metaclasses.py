# class
class BankAccount(object):
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            return "Not enough balance"
        self.balance -= amount
        return f"{amount} withdrawn! Current balance => {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. Current balance => {self.balance}"
    
    def check_balance(self):
        return f"Current balance {self.balance}"

# object
account_1 = BankAccount(500)
# operations over instantiated object
print(account_1)
print(account_1.check_balance())
print(account_1.deposit(20))
print(account_1.withdraw(30))

print(type(account_1))
print(account_1.__class__)
print(account_1.__class__.__class__)

print(dir(BankAccount))
print(dir(BankAccount.__class__))
print(dir(type))

TypeBankAccount = type(
    "BankAccount",
    (),
    {
        "bank_balance": 500,
        "account_holder": "John Doe",
        "__str__": lambda self: f"{self.account_holder} have {self.bank_balance}"
    }
)

t = TypeBankAccount()

print(t)
print(type(t))
print(t.account_holder, t.bank_balance)
print(dir(t))

# inheritance

TypeInheritedBankAccount = type(
    "InheritedBankAccount",
    (BankAccount, ),
    {
        "bank_balance": 500,
        "account_holder": "John Doe",
        "__str__": lambda self: f"{self.account_holder} have {self.bank_balance}, inherited balance {self.balance}"
    }
)
ti = TypeInheritedBankAccount(balance=500)
print(ti)
print(type(ti))
print(ti.account_holder, ti.bank_balance, ti.balance)
print(dir(ti))