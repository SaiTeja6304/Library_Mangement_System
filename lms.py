from flask import Flask, redirect, render_template, request, session

import lmsController
from flask_session import Session
import login
from lmsController import libraryController

# for database the class is imported
from books_model import booksModel

# Initial command
app = Flask(__name__)

# For database connection
db = booksModel("lib.db")

# Creating login object by calling login filename with Login class name created in login file,
# app is parameter
lp = login.Login(app)

# Creating library controller object
lc = lmsController.libraryController(app)

# Configuring the routes for login
app.add_url_rule("/", view_func=lp.index)
app.add_url_rule("/login", methods=['GET', 'POST'], view_func=lp.login)
app.add_url_rule("/logout", view_func=lp.logout)

# Configuring routes for library controller
app.add_url_rule("/view-bookpg", view_func=lc.view_books)
app.add_url_rule("/add-bookpg", view_func=lc.add_books)
app.add_url_rule("/rem-bookpg", view_func=lc.remove_books)
app.add_url_rule("/update-bookpg", view_func=lc.update_books)
app.add_url_rule("/borrow-bookpg", view_func=lc.borrow_books)
app.add_url_rule("/export-filepg", view_func=lc.export_file)
app.add_url_rule("/pdf-generatorpg", view_func=lc.pdf_generator)
app.add_url_rule("/book-added", methods=['GET', 'POST'], view_func=lc.add_books_return)
app.add_url_rule("/update-pg/<string:BID>", methods=['GET', 'POST'], view_func=lc.show_update_infopg)
app.add_url_rule("/books-update", methods=['GET', 'POST'], view_func=lc.update_after)

# Settings for creating session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Command to run the application
if __name__ == "__main__":
    app.run()