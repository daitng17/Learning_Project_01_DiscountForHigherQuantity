# basic class definition

class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # instance methods
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price*self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

# create instances of the class
b1 = Book('Great Day', 'Thanh Nguyen', 345, 2000)
b2 = Book('Fresh Start', 'Jaime Nguyen', 244, 3454)

print(b1.getprice())
b2.setdiscount(0.25)
print(b2.getprice())