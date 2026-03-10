class BankAccount:

    def __init__(self, owner, balance): #Constructor Parameter Should Not Be Private

        self.owner = owner
        self.__balance = balance 

    def deposit(self, d_amount):
        if d_amount <= 0:
            return "Error, Negative and Nill deposits are not allowed !!"
        else:
            self.__balance += d_amount

    def withdraw(self, w_amount):
        if w_amount <=0 :
            return "Error, Negative and Nill Withdrawals are not allowed !!"
        elif w_amount > self.__balance:
            return "Insufficent Balance !!"
        else:
            self.__balance -= w_amount

    def get_balance(self):
        print(f"Your current balance is : {self.__balance}")

Cl1 = BankAccount("Ram", 10000)
Cl1.get_balance()
Cl1.deposit(10000)
Cl1.withdraw(5000)
Cl1.get_balance()
