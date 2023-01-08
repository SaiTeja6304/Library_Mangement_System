import sqlite3

class booksModel():
    def __init__(self, app):
        self.conn = sqlite3.connect("lib.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS books (bookid TEXT PRIMARY KEY, 
        authorname TEXT NOT NULL, bookname TEXT NOT NULL, genre TEXT NOT NULL, quantity INTEGER,
        price INTEGER)""")
        self.conn.commit()

    def add_book(self, books):
        authname = books.get_authorname()
        bname = books.get_bookname()
        bgenre = books.get_genre()
        bquantity = books.get_quantity()
        bprice = books.get_price()

        self.cur.execute('SELECT MAX(rowid) as "mid [integer]" FROM books')
        rows = self.cur.fetchone()[0]
        bid = rows

        if bid == None:
            bid = 1
        else:
            bid = bid + 1

        fbid = 'BOOK' + str(bid)

        self.cur.execute("INSERT INTO books (bookid, authorname, bookname, genre, quantity, price) VALUES(?, ?, ?, ?, ?, ?)", (fbid, authname, bname, bgenre, bquantity, bprice))
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from books")
        bdata = self.cur.fetchall()
        return bdata

    def update_bookinfo(self, BID):
        self.cur.execute("SELECT * FROM books where bookid=?", (BID,))
        updatedata = self.cur.fetchall()
        return updatedata

    def update_book(self, books, bid):
        authname = books.get_authorname()
        bname = books.get_bookname()
        bgenre = books.get_genre()
        bquantity = books.get_quantity()
        bprice = books.get_price()

        self.cur.execute("UPDATE books SET authorname = ?, bookname = ?, genre = ?, quantity = ?, price = ? WHERE bookid = ?", (authname, bname, bgenre, bquantity, bprice, bid))
        self.conn.commit()

    def delete_book(self, bId):
        self.cur.execute("DELETE FROM books WHERE bookid=?", (bId,))
        self.conn.commit()


    def __del__(self):
        self.cur.close()
        self.conn.close()