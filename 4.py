class BankAccount:


  def __init__(self, account_number, account_holder):

    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = 0.0  # Initialize balance to 0.0

  def deposit(self, amount):

    self.balance += amount
    print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

  def withdraw(self, amount):

    if amount > self.balance:
      print(f"Insufficient funds. Available balance: ${self.balance:.2f}")
    else:
      self.balance -= amount
      print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

  def get_balance(self):

    return self.balance

  def __str__(self):

    return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance:.2f}"

class SavingsAccount(BankAccount):


  def __init__(self, account_number, account_holder, interest_rate):

    super().__init__(account_number, account_holder)
    self.interest_rate = interest_rate

  def apply_interest(self):

    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

  def __str__(self):

    return super().__str__() + f"\nInterest Rate: {self.interest_rate:.2%}"  # Display interest rate as a percentage

# Create a BankAccount instance
my_account = BankAccount("12345678", "John Doe")

# Deposit $1000
my_account.deposit(1000.00)

# Withdraw $500
my_account.withdraw(500.00)

# Print current balance (should be $500.00)
print(my_account)

# Create a SavingsAccount instance with 2% interest
savings = SavingsAccount("87654321", "Jane Smith", 0.02)

# Deposit $1500
savings.deposit(1500.00)

# Apply interest
savings.apply_interest()

# Print current balance and interest rate (should be $1530.00 and 2.00%)
print(savings)
