# Program by Nick NguyenDaiTruongThanh
# Intern Parts Pricing, Finance & Controlling, MFTBC

class PartsPricing():
    '''This class consists of functions used to calculate list price (lp),
    discount percent (d), net price factor (npf), and dealer price (dp).'''

    def __init__(self, lp):
        self.lp = lp

    # calculation methods

    def price(self):
        if hasattr(self, '_discount'):
            return (self.lp - (self.lp * self._discount))
        else:
            return self.lp

    def netfactor(self):
        if hasattr(self, '_discount'):
            return 1 - self._discount
        else:
            return 0
    
    def discountprice(self, d):
        self._discount = d

# test with individual parts

engine1 = PartsPricing(2000)
engine2 = PartsPricing(1600)
print(engine1.price())
engine1.discountprice(0.6)
print(engine1.price())
print(engine1.netfactor())

# test with a list of part

pricelist = (1000, 2000, 500)

for e in pricelist:
    pri = PartsPricing(e)
    pri.discountprice(0.7)
    print(pri.price())



'''LP = 2000
    D = 0.6
    F = 0.4
   DP = 800'''

