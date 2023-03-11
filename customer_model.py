import sqlite3

class customerModel():
    def __init__(self, app):
        self.conn = sqlite3.connect("lib.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS customers (custid TEXT PRIMARY KEY, 
                custname TEXT NOT NULL, emailid TEXT NOT NULL, pnum TEXT NOT NULL, 
                address TEXT NOT NULL, booklist TEXT NOT NULL)""")
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
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()