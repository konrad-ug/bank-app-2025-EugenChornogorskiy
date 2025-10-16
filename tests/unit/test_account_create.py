from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe","12345678901")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "12345678901"
    def test_krotki_pesel(self):
        account = Account("John", "Doe","1234567890")
        assert account.pesel == "Invalid"
    def test_dlugi_pesel(self):
        account = Account("John", "Doe","123456789012")
        assert account.pesel == "Invalid"
    def test_dlugi_pesel(self):
        account = Account("John", "Doe", None)
        assert account.pesel == "Invalid"
        