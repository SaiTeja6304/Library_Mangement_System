from flask import render_template, redirect, request, app, flash

class customer():
    def __init__(self, app):
        pass

    def view_customers(self):
        return render_template("view_customers.html")

    def add_customer(self):
        return render_template("add_customer.html")

    def customer_actions(self):
        return render_template("customer_actions.html")

    def borrow_book(self):
        return render_template("borrow_book.html")

    def view_borrowers(self):
        return render_template("view_borrowers.html")