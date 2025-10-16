class Account:
    def __init__(self, first_name, last_name, pesel = None, promo = None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 50.0 if self.is_promo_valid(promo) else 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid" 
    def is_pesel_valid(self,pesel):
        if isinstance(pesel,str) and (len(pesel) == 11):
            return True 
    def is_promo_valid(self,promo):
        if promo and promo.startswith("PROM_") and len(promo) == 8:
            return True
        