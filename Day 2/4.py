#  Implement a class BankAccount that:       
# Uses encapsulation for balance (private variable).
# Provides public methods deposit, withdraw, and get_balance.
# Add docstrings to simulate abstraction.

class BankAccount:
    """
    BankAccount represents a simple bank account.

    Abstraction:
    - The internal balance is hidden from the user.
    - Users interact with the account only through public methods
      such as deposit(), withdraw(), and get_balance().
    """

    def __init__(self, initial_balance=0):
        """
        Initialized the bank account with an optional initial balance.
        """
        self.__balance = initial_balance  
    def deposit(self, amount):
        """
        Deposit a positive amount into the account.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount if sufficient balance exists.
        """
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        """
        Return the current account balance.
        """
        return self.__balance
account = BankAccount(500)
account.deposit(350)
account.withdraw(130)

print("Current Balance:", account.get_balance())
        