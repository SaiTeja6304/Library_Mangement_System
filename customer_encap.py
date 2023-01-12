class Customer:
    def __init__(self, custname, emailid, phnum, address, booklist):
        self.custname = custname
        self.emailid = emailid
        self.phnum = phnum
        self.address = address
        self.booklist = booklist

    # setter methods
    def set_custname(self, custname):
        self._custname = custname

    def set_emailid(self, emailid):
        self._emailid = emailid

    def set_phnum(self, phnum):
        self._phnum = phnum

    def set_address(self, address):
        self._address = address

    def set_booklist(self, booklist):
        self._booklist = booklist


    # getter methods
    def get_custname(self):
        return self._custname

    def get_emailid(self):
        return self._emailid

    def get_phnum(self):
        return self._phnum

    def get_address(self):
        return self._address

    def get_booklist(self):
        return self._booklist