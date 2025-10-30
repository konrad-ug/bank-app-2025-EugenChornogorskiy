class Account:
    def __init__(self):
        self.balance = 0.0
        self.fee = 0.0
    def incoming_transfer(self,amount):
        self.balance += amount 
    def outgoing_transfer(self,amount,express=None):
        if (self.balance >= amount):
            if(express):
                self.balance -= (amount +self.fee)
            else:
                self.balance -= amount

        
