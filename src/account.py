class Account:
    def __init__(self, first_name, last_name, pesel = None, promo = None):
        self.first_name = first_name
        self.last_name = last_name 
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid" 
        self.balance = 50.0 if self.is_promo_valid(promo) and self.is_eligible_for_promo() else 0.0
    def is_pesel_valid(self,pesel):
        if isinstance(pesel,str) and (len(pesel) == 11):
            return True 
    def is_promo_valid(self,promo):
        if promo and promo.startswith("PROM_") and len(promo) == 8:
            return True
    def get_birth_year_from_pesel(self): 
        if not self.is_pesel_valid(self.pesel):
            return None
        year = int(self.pesel[:2])
        month = int(self.pesel[2:4])
        if month > 80: 
            year += 1800
        elif month > 60: 
            year += 2200
        elif month > 40: 
            year += 2100
        elif month > 20: 
            year += 2000
        else: 
            year += 1900
        return year 
    def is_eligible_for_promo(self): 
        birth_year = self.get_birth_year_from_pesel()
        return birth_year is not None and birth_year > 1960