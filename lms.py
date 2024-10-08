from flask import Flask, redirect, render_template, request, session

import lmsController
from flask_session import Session
import login
import customerController

# for database the class is imported
from books_model import booksModel
from customer_model import customerModel

# Initial command
app = Flask(__name__)

# For database connection
db = booksModel("lib.db")
db2 = customerModel("lib.db")

# Creating login object by calling login filename with Login class name created in login file,
# app is parameter
lp = login.Login(app)

# Creating library controller object
lc = lmsController.libraryController(app)

# Creating customer controller object
cc = customerController.customer(app)

# Configuring the routes for login
app.add_url_rule("/", view_func=lp.index)
app.add_url_rule("/login", methods=['GET', 'POST'], view_func=lp.login)
app.add_url_rule("/logout", view_func=lp.logout)

# Configuring routes for library controller
app.add_url_rule("/view-bookpg", view_func=lc.view_books)
app.add_url_rule("/add-bookpg", view_func=lc.add_books)
app.add_url_rule("/rem-bookpg", view_func=lc.remove_books)
app.add_url_rule("/update-bookpg", view_func=lc.update_books)
app.add_url_rule("/borrow-availpg", view_func=lc.books_available)
app.add_url_rule("/export-filepg", view_func=lc.export_file)
app.add_url_rule("/pdf-generatorpg", view_func=lc.pdf_generator)
app.add_url_rule("/customer-actions", view_func=lc.show_customer_actions)
app.add_url_rule("/book-added", methods=['GET', 'POST'], view_func=lc.add_books_return)
app.add_url_rule("/update-pg/<string:BID>", methods=['GET', 'POST'], view_func=lc.show_update_infopg)
app.add_url_rule("/books-update", methods=['GET', 'POST'], view_func=lc.update_after)
app.add_url_rule("/delete-book", methods=['GET', 'POST'], view_func=lc.remove_action)
app.add_url_rule("/check-book", methods=['GET', 'POST'], view_func=lc.check_book_availability)
app.add_url_rule("/check-book-by-name", methods=['GET', 'POST'], view_func=lc.check_book_avail_by_name)
app.add_url_rule("/export-books", view_func=lc.export_books)
app.add_url_rule("/gen-pdf-bk", view_func=lc.generate_pdf_books)

# customer routing
app.add_url_rule("/view-customerspg", view_func=cc.view_customers)
app.add_url_rule("/add-customerpg", view_func=cc.add_customer)
app.add_url_rule("/customer-actionspg", view_func=cc.customer_actions)
app.add_url_rule("/borrow-bookpg", view_func=cc.borrow_book)
app.add_url_rule("/view-borrowerspg", view_func=cc.view_borrowers)
app.add_url_rule("/customer-added", methods=['GET', 'POST'], view_func=cc.customer_added)
app.add_url_rule("/update-custpg/<string:CustID>", methods=['GET', 'POST'], view_func=cc.upd_cust)
app.add_url_rule("/customer-update", methods=['GET', 'POST'], view_func=cc.upd_cust_after)
app.add_url_rule("/delete-cust", methods=['GET', 'POST'], view_func=cc.delete_customer)
app.add_url_rule("/check-cid-borrow", methods=['GET', 'POST'], view_func=cc.check_valid_customer)
app.add_url_rule("/borrow-success", methods=['GET', 'POST'], view_func=cc.add_borrower)
app.add_url_rule("/delete-borrow", methods=['GET', 'POST'], view_func=cc.return_borrow)
app.add_url_rule("/mail-borrow", methods=['GET', 'POST'], view_func=cc.send_email)
app.add_url_rule("/export-cust", view_func=cc.export_customers)
app.add_url_rule("/export-borrow", view_func=cc.export_borrowers)
app.add_url_rule("/gen-pdf-cust", view_func=cc.generate_pdf_custs)

# Settings for creating session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Command to run the application
if __name__ == "__main__":
    app.run()