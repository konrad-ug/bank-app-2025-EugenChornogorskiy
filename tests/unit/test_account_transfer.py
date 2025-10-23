from src.personal_account import Personal_Account


class TestAccount:
    def setup_method(self):
       self.exp_account = Personal_Account("John", "Doe")  
    def test_incoming_transfer(self):
        self.exp_account.incoming_transfer(100)
        assert self.exp_account.balance == 100 
    def test_outgoing_transfer(self):
        self.exp_account.balance = 200
        self.exp_account.outgoing_transfer(50)
        assert self.exp_account.balance == 150 
    def test_no_money(self):
        self.exp_account.outgoing_transfer(1000)
        assert self.exp_account.balance == 0
    def test_express_transfer(self):
        self.exp_account.balance = 200
        self.exp_account.outgoing_transfer(100,"express")
        assert self.exp_account.balance == 99