class BankAccount:
    def __init__(self, name = "Dupont", balance = 1000):
        self.name = name 
        self.balance = balance

    def deposit(self, value):
        self.balance += value 
     
    def withdrawal(self, value):
        self.balance -= value 

    def show(self):
        print("The balance of " + self.name+" 's bank account is "+str(self.balance)+" euros")



account1 = BankAccount("Duchmol", 800)
account1.deposit(350)
account1.withdrawal(200)
account1.show()
account2 = BankAccount()
account2.deposit(25)
account2.show()

