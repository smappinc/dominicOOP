class BankAccount:

    # Class variable
    interest_rate = 0.05

    # Constructor for the class BankAccount with balance set to 0
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    # A method that adds a specified amount to balance variable
    def deposit(self, amount):
        
        # An if statement to check where the deposit is more than 0.
        if amount > 0:
            self.balance += amount
            print(f"Hello {self.account_holder}, you have deposited {amount} into your account.\n")
        else:
            print(f"You need to deposit more than 0")

    # A method that subtracts a specified amount to balance variable
    def withdraw(self, amount):

        # This if statement checks whether the balance is sufficient to make a withdraw
        if self.balance > 0:
            self.balance -= amount 
        else:
            print(f"\nYou have insufficient Funds. Please deposit")

    # Applying interest to the balance
    def applyinterest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"-----interest applied to {self.account_holder}: {interest}\n")

    # Displaying account Information
    def display_account_info(self):
        print(f"Hello {self.account_holder}:\n Your account balance is ${self.balance}\n")


# Two Objects of the class BankAccount
nancy_account = BankAccount("Nancy Cullingnan Sentogo")
ben_account = BankAccount("Ben Muhoozi")

#deposit and withdraws
nancy_account.deposit(5000)
nancy_account.withdraw(4500)

ben_account.deposit(4000)
ben_account.withdraw(3000)

#Applying interest
nancy_account.applyinterest()
ben_account.applyinterest()

#Displaying Account Info
nancy_account.display_account_info()
ben_account.display_account_info()


