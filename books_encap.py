class Books:
    def __init__(self, authorname, bookname, genre, quantity, price):
        self.authorname = authorname
        self.bookname = bookname
        self.genre = genre
        self.quantity = quantity
        self.price = price

    # setter methods
    def set_authorname(self, authorname):
        self._authorname = authorname

    def set_bookname(self, bookname):
        self._bookname = bookname

    def set_genre(self, genre):
        self._genre = genre

    def set_quantity(self, quantity):
        self._quantity = quantity

    def set_price(self, price):
        self._price = price

    # getter methods
    def get_authorname(self):
        return self._authorname

    def get_bookname(self):
        return self._bookname

    def get_genre(self):
        return self._genre

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price