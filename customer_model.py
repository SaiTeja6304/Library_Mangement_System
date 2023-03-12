import sqlite3

class customerModel():
    def __init__(self, app):
        self.conn = sqlite3.connect("lib.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS customers (custid TEXT PRIMARY KEY, 
                custname TEXT NOT NULL, emailid TEXT NOT NULL, pnum TEXT NOT NULL, 
                address TEXT NOT NULL, booklist TEXT NOT NULL)""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS borrowers(custid TEXT NOT NULL, 
        custname TEXT NOT NULL, bkname TEXT NOT NULL, returndate DATE, 
        FOREIGN KEY(custid) REFERENCES customers(custid))""")
        self.conn.commit()

    def add_cust(self, custs):
        custname = custs.get_custname()
        custemail = custs.get_emailid()
        custnum = custs.get_phnum()
        custaddr = custs.get_address()
        custbooklist = custs.get_booklist()

        self.cur.execute('SELECT MAX(rowid) as "mid [integer]" FROM customers')
        rows = self.cur.fetchone()[0]
        custid = rows

        if custid == None:
            custid = 1
        else:
            custid = custid + 1

        fcustid = 'CUSTOMER' + str(custid)

        self.cur.execute("INSERT INTO customers (custid, custname, emailid, pnum, address, booklist) VALUES(?, ?, ?, ?, ?, ?)", (fcustid, custname, custemail, custnum, custaddr, custbooklist))
        self.conn.commit()

    def fetch_cust(self):
        self.cur.execute("SELECT * FROM customers")
        custdata = self.cur.fetchall()
        return custdata

    def update_custinfo(self, CustID):
        self.cur.execute("SELECT * FROM customers WHERE custid=?", (CustID,))
        updcust = self.cur.fetchall()
        return updcust

    def update_cust(self, custs, custid):
        updcustname = custs.get_custname()
        updcustemail = custs.get_emailid()
        updcustnum = custs.get_phnum()
        updcustaddr = custs.get_address()
        updbooklist = custs.get_booklist()

        self.cur.execute("UPDATE customers SET custname=?, emailid=?, pnum=?, address=?, booklist=? WHERE custid=?", (updcustname, updcustemail, updcustnum, updcustaddr, updbooklist, custid))
        self.conn.commit()

    def delete_cust(self, cid):
        self.cur.execute("DELETE FROM customers where custid=?", (cid,))
        self.cur.execute("DELETE FROM borrowers WHERE custid=?", (cid,))
        self.conn.commit()

    def valid_cust(self, cid):
        self.cur.execute("SELECT * FROM customers where custid=?", (cid,))
        ciddata = self.cur.fetchall()
        return ciddata

    def borrower(self, custid, custname, bkname, rtndt):
        self.cur.execute("INSERT INTO borrowers (custid, custname, bkname, returndate) VALUES (?, ?, ?, ?)", (custid, custname, bkname, rtndt))
        self.conn.commit()

    def add_booklist(self, custid, bkname):
        self.cur.execute("SELECT booklist FROM customers WHERE custid=?", (custid,))
        booklist = self.cur.fetchall()
        newlist = "0"
        if len(booklist[0][0]) == 0:
            newlist = booklist[0][0] + str(bkname)
        else:
            newlist = booklist[0][0] + ", " + str(bkname)
        self.cur.execute("UPDATE customers SET booklist=? WHERE custid=?", (newlist, custid))
        self.conn.commit()

    def fetch_borrowers(self):
        self.cur.execute("SELECT * FROM borrowers")
        borrowdata = self.cur.fetchall()
        return borrowdata

    def del_borrow(self, custid, bkname):
        self.cur.execute("DELETE FROM borrowers WHERE custid=? AND bkname=?", (custid, bkname))
        self.conn.commit()

    def fetch_email(self, custid):
        self.cur.execute("SELECT emailid FROM customers WHERE custid=?", (custid,))
        email = self.cur.fetchall()
        return email

    def export_cust(self):
        self.cur.execute("SELECT * FROM customers")
        custdata = self.cur.fetchall()
        return custdata

    def export_borrow(self):
        self.cur.execute("SELECT * FROM borrowers")
        borrowdt = self.cur.fetchall()
        return borrowdt

    def __del__(self):
        self.cur.close()
        self.conn.close()