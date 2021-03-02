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

# test with a list of parts

pricelist = [1000, 2000, 500]

for e in pricelist:
    pri = PartsPricing(e)
    pri.discountprice(0.7)
    print(pri.price())

# test with a dict of different parts and prices

pricedict = {'en1' : [1000, 0.6], 'en2' : [2000, 0.5], 'en3' : [500, 0.7]}

for k, v in pricedict.items():
    pri = PartsPricing(v[0])
    pri.discountprice(v[1])
    print(k + ':' + str(pri.price()))



