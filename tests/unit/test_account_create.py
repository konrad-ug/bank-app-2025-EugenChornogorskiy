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
        account = Account("John", "Doe")
        assert account.pesel == "Invalid"
    def test_correct_promo(self):
        account = Account("John", "Doe","12345678901","PROM_XYZ")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 50.0
    def test_long_promo(self):
        account = Account("John", "Doe","12345678901","PROM_XYZZ")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0       
    def test_short_promo(self):
        account = Account("John", "Doe","12345678901","PROM_XY")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0  
    def test_short_promo(self):
        account = Account("John", "Doe","12345678901","PRO_XYZZ")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0  
    def test_promo_valid_for_young_person(self): 
        acc = Account("Jan", "Kowalski", pesel="70010112345", promo="PROM_123")
        assert acc.balance == 50.0

    def test_promo_invalid_for_old_person(self): 
        acc = Account("Anna", "Nowak", pesel="50010112345", promo="PROM_123")
        assert acc.balance == 0.0

    def test_no_promo(self):
        acc = Account("Piotr", "Zieliński", pesel="70010112345", promo=None)
        assert acc.balance == 0.0

    def test_invalid_pesel(self):
        acc = Account("Maria", "Wiśniewska", pesel="123", promo="PROM_123")
        assert acc.pesel == "Invalid" 
        assert acc.balance == 0.0

    def test_invalid_promo_format(self):
        acc = Account("Kasia", "Lewandowska", pesel="70010112345", promo="BADPROMO")
        assert acc.balance == 0.0
