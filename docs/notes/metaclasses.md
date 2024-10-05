# Metaclass 💫 - Lowest of Python classes 

My colleague, Mr. Ramesh, asked me a question "what is the lowest of all classes in Python?". I, obviously, said it has to be `object` as I have come across some classes inherited from that. To my surprise, I was wrong, that too not anywhere near the correct answer. Let's figure out the correct answer.

## Object vs Class

Even though this is the basic which almost everyone aware of, it seems to be a right place to begin with. 

Class is a blueprint/template/signature, with which an object can be created. 

So, if you need to store data of a Bank Account along with methods to withdraw and deposit money, you need to design a class which stores necessary information of a Bank account, and have two methods `withdraw` and `deposit` to encapsulate the class attribute `account_balance`. 

```py title="metaclasses.py"

# class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            return "Not enough balance"
        self.balance -= amount
        return f"{amount} withdrawn!"
    
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. Current balance => {self.balance}"
    
    def check_balance(self):
        return f"Current balance {self.balance}"

# object
account_1 = BankAccount(500)
# operations over instantiated object
print(account_1)
# O/P => <__main__.BankAccount object at 0x104b0c980>
print(account_1.check_balance())
# O/P => Current balance 500
print(account_1.deposit(20))
# O/P => 20 deposited. Current balance => 520
print(account_1.withdraw(30))
# O/P => 30 withdrawn! Current balance => 490
```
From the above example, you can see that `BankAccount` class provides necessary information about the attributes needed to instantiate an object with the class and actions which can be performed over the class. 

Once you instantiate the class with needed attribute, it becomes an object. That's all! 

## Tracking the root of declared class

Let's consider the above code to trace it back to the lowest level of declaration possible. 

Before that, I believe you are aware of how to check the class of an instantiated object. We can use the namespace `type` or `.__class__` of the object.

```py
type(account_1)
# O/P => <class '__main__.BankAccount'>
account_1.__class__
# O/P => <class '__main__.BankAccount'>
```

`account_1` is an instance derived from `BankAccount` class. Neat ✅. Let's go one node further. What was the root for class `BankAccount`?

```py
account_1.__class__.__class__
# O/P => <class 'type'>
```

What in green earth this is? `BankAccount` class is a class of `type` class? 🤯

## What are metaclasses?

Welcome to the world of metaclasses. On a higher level, metaclasses are what I use to differentiate the role of developers and programmers (Programmers != Developers. Yeah, a different debate altogether). 

Metaclasses, as the name suggests, are the blueprints for creating classes 😵‍💫. Not clear? Let me try to make it clear. 

So, `BankAccount` is the set of rules to create a bank account and contains of the possible set of actions with the class. Is this clear? You can use `dir` to confirm this point.

```py
dir(BankAccount)
# O/P => ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'check_balance', 'deposit', 'withdraw']
```
So what defines the behaviors of a `class` object? Where are the definitions of `dunder methods` and other actions of a class? `type` metaclass holds the set of rules for that. Let's check the attributes of type.

```py
dir(type)
# O/P => ['__abstractmethods__', '__annotations__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__or__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__type_params__', '__weakrefoffset__', 'mro']
```

Interesting, isn't it? You can understand that `BankAccount` is **not inherited** from `type`, but **instantiated** from. Otherwise, all methods and attributes of `type` should have been available in our class as well.

## Can you create a python object without built-in class keyword? 🤔
Yes, a hundred times yes. A little tricky, but yes. Using `type` metaclass, you can create an object. 

```py
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
# O/P => John Doe have 500
print(type(t))
# O/P => <class '__main__.BankAccount'>
print(t.account_holder, t.bank_balance)
# O/P => John Doe 500
print(dir(t))
# O/P => ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'account_holder', 'bank_balance']
```

Additionally, we can inherit other classes also. Let's instantiate an object `TypeInheritedBankAccount` from `BankAccount`. 

```py
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
# O/P => John Doe have 500, inherited balance 500
print(type(ti))
# O/P => <class '__main__.InheritedBankAccount'>
print(ti.account_holder, ti.bank_balance, ti.balance)
# O/P => John Doe 500 500
print(dir(ti))
# O/P => ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'account_holder', 'balance', 'bank_balance', 'check_balance', 'deposit', 'withdraw']
```

Voilà! 🎉

## Why and Where to use metaclasses?

Honestly, I couldn't wrap my head around this 😧. I am reading about it, will update this section once I am convinced about my understanding. 

<details>
<summary>Summed up code of different sections </summary>
    ```py title="metaclasses.py"
    
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
    ```
</details>

## References
- [Are meta classes the HARDEST thing in Python? by Carberra](https://www.youtube.com/watch?v=zsPZPi39Xvo&t=593s)
- [What are Python metaclasses?](https://sentry.io/answers/what-are-Python-metaclasses/)
- [Metaclasses in Python](https://www.youtube.com/watch?v=yWzMiaqnpkI)