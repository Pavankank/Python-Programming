from abc import ABC

class Bank(ABC):
    def getRateofInterest(self):
        pass

class icici(Bank):
    def getRateofInterest(self):
        # return super().getRateofInterest()
        print("icici offers 7% rate")

class kotak(Bank):
    def getRateofInterest(self):
        # return super().getRateofInterest()
        print("Kotak offers 8.5% rate")

c = icici
k = kotak

c.getRateofInterest()
k.getRateofInterest()