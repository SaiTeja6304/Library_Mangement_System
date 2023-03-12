import json
import os
import smtplib
import csv
from fpdf import FPDF
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

    def check_valid_customer(self):
        if request.method == "GET":
            cid = request.args.get("custId")
            cm = customerModel(app)
            ciddata = cm.valid_cust(cid)
            return json.dumps(ciddata)

    def add_borrower(self):
        if request.method == "POST":
            if request.form.get("borrow-confirm"):
                custid = request.form.get("custid")
                custname = request.form.get("custname")
                bkname = request.form.get("bkname")
                rtndt = request.form.get("rtndt")

                cm = customerModel(app)
                cm.borrower(custid, custname, bkname, rtndt)
                cm.add_booklist(custid, bkname)

                flash("Borrow Successfully", "info")
                return redirect("/customer-actions")

    def view_borrowers(self):
        cm = customerModel(app)
        borrowdata = cm.fetch_borrowers()
        return render_template("view_borrowers.html", borrowdata = borrowdata)

    def return_borrow(self):
        if request.method == "GET":
            custid = request.args.get("custId")
            bkname = request.args.get("bkname")

            cm = customerModel(app)
            cm.del_borrow(custid, bkname)

            return custid, bkname

    def send_email(self):
        if request.method == "GET":
            custid = request.args.get("custid")
            custname = request.args.get("custname")
            bkname = request.args.get("bkname")
            date = request.args.get("rtndt")

            cm = customerModel(app)
            email = cm.fetch_email(custid)

            EMAIL_ADDRESS = os.environ.get('MAIL_DEFAULT_SENDER')
            EMAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                subject = 'Library Remainder'
                body = f"""Dear Customer \n {custname}, This is a remainder to return the borrowed 
                book {bkname} from library by the date:{date} \n Thank you for using our 
                library resources\n For any further queries please contact +919885983806"""

                msg = f'Subject: {subject}\n\n {body}'

                smtp.sendmail(EMAIL_ADDRESS, email, msg)

            return custid

    def export_customers(self):
        cm = customerModel(app)
        filename = "customers"
        myfilename = filename + ".csv"
        with open(myfilename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Custid', 'Custname', 'Emailid', 'Phone Number', 'Address', 'Booklist'])
            writer.writerows(cm.export_cust())
        flash("CSV Generated Successfully", "info")
        return redirect("/export-filepg")

    def export_borrowers(self):
        cm = customerModel(app)
        filename = "borrowers"
        myfilename = filename + ".csv"
        with open(myfilename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Custid', 'Custname', 'Book Name', 'Return Data'])
            writer.writerows(cm.export_borrow())
        flash("CSV Generated Successfully", "info")
        return redirect("/export-filepg")

    def generate_pdf_custs(self):
        # create pdf object
        pdf = FPDF('P', 'mm', 'Letter')
        # add a page
        pdf.add_page()
        # set font and size
        pdf.set_font('times', '', 16)
        cm = customerModel(app)
        custdt = cm.export_cust()
        pdf.cell(150, 20, "Custid, Custname, Emailid, Phone Number, Address, Booklist", ln=True, border=True)
        for cust in custdt:
            # insert data into pdf
            pdf.cell(150, 20, str(cust), ln=True, border=True)

        # create pdf and name it
        pdf.output('customers.pdf')
        flash("PDF Generated Successfully", "info")
        return redirect("/pdf-generatorpg")
