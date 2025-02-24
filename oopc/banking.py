class Bank:
  bank_name = ""
  balance = 0

  def deposit(self,amount):
    self.balance = self.balance + amount
    print("Amount Debited")

  def withdraw(self,amount):
    self.balance = self.balance - amount
    print("Amount Credited")

b1 = Bank()
b1.bank_name = "SBI"
b1.balance = 10000
b1.deposit(5000)
b1.withdraw(2000)

print(b1.balance)
