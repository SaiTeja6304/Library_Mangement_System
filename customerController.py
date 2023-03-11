from flask import render_template, redirect, request, app, flash
from customer_model import customerModel
from customer_encap import Customer

class customer():
    def __init__(self, app):
        pass

    def view_customers(self):
        cm = customerModel(app)
        custdata = cm.fetch_cust()
        return render_template("view_customers.html", custdata = custdata)

    def add_customer(self):
        return render_template("add_customer.html")

    def customer_added(self):
        if request.method == "POST":
            if request.form.get("add-cust"):
                custname = request.form.get("custname")
                custemail = request.form.get("custemail")
                custnum = request.form.get("custnum")
                custaddr = request.form.get("custaddr")
                booklist = ""

                cust = Customer(custname, custemail, custnum, custaddr, booklist)
                cust.set_custname(custname)
                cust.set_emailid(custemail)
                cust.set_phnum(custnum)
                cust.set_address(custaddr)
                cust.set_booklist(booklist)

                cm = customerModel(app)
                cm.add_cust(cust)

                flash("Customer Added Successfully", "info")
                return redirect("/customer-actions")

    def customer_actions(self):
        cm = customerModel(app)
        custdata = cm.fetch_cust()
        return render_template("customer_actions.html", custdata = custdata)

    def upd_cust(self, CustID):
        cm = customerModel(app)
        updcust = cm.update_custinfo(CustID)
        print(updcust)
        return render_template("update_customerpg.html", udata = updcust)

    def upd_cust_after(self):
        if request.method == "POST":
            if request.form.get("upd-cust"):
                updcustname = request.form.get("updcustname")
                updcustemail = request.form.get("updcustemail")
                updcustnum = request.form.get("updcustnum")
                updcustaddr = request.form.get("updcustaddr")
                updbooklist = request.form.get("updbooklist")
                updcustid = request.form.get("updcustid")

                cust = Customer(updcustname, updcustemail, updcustnum, updcustaddr, updbooklist)
                cust.set_custname(updcustname)
                cust.set_emailid(updcustemail)
                cust.set_phnum(updcustnum)
                cust.set_address(updcustaddr)
                cust.set_booklist(updbooklist)

                cm = customerModel(app)
                cm.update_cust(cust, updcustid)

                flash("Customer Updated Successfully", "info")
                return redirect("/customer-actions")

    def delete_customer(self):
        if request.method == "GET":
            cId = request.args.get("cId")
            cm = customerModel(app)
            cm.delete_cust(cId)
        return cId

    def borrow_book(self):
        return render_template("borrow_book.html")

    def view_borrowers(self):
        return render_template("view_borrowers.html")

