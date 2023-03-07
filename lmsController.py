import json

from flask import render_template, redirect, request, app, flash
from books_model import booksModel
from books_encap import Books

class libraryController():

    def __init__(self, app):
        pass

    def view_books(self):
        bm = booksModel(app)
        bookdata = bm.fetch()
        return render_template("view_books.html", libdata = bookdata)

    def add_books(self):
        return render_template("add_books.html")

    def add_books_return(self):
        if request.method == "POST":
            if request.form.get("add-book"):
                authname = request.form.get("authname")
                bookname = request.form.get("bname")
                genre = request.form.get("bgenre")
                quantity = request.form.get("bquantity")
                price = request.form.get("bprice")

                books = Books(authname, bookname, genre, quantity, price)
                books.set_authorname(authname)
                books.set_bookname(bookname)
                books.set_genre(genre)
                books.set_quantity(quantity)
                books.set_price(price)

                bm = booksModel(app)
                bm.add_book(books)

                flash("Book Added Successfully", "info")
                return redirect("/")

    def remove_books(self):
        bm = booksModel(app)
        bookdata = bm.fetch()
        return render_template("remove_books.html", libdata = bookdata)

    def remove_action(self):
        if request.method == "GET":
            bId = request.args.get("bId")
            bm = booksModel(app)
            bm.delete_book(bId)
        return bId

    def update_books(self):
        bm = booksModel(app)
        bookdata = bm.fetch()
        return render_template("update_books.html", libdata = bookdata)

    def show_update_infopg(self, BID):
        bm = booksModel(app)
        updbdata = bm.update_bookinfo(BID)
        return render_template("update_bookspg.html", udata = updbdata)

    def update_after(self):
        if request.method == "POST":
            if request.form.get("upd-book"):
                uauthname = request.form.get("updauthname")
                ubookname = request.form.get("updbname")
                ugenre = request.form.get("updbgenre")
                uquantity = request.form.get("updbquantity")
                uprice = request.form.get("updbprice")
                ubid = request.form.get("updbid")

                books = Books(uauthname, ubookname, ugenre, uquantity, uprice)
                books.set_authorname(uauthname)
                books.set_bookname(ubookname)
                books.set_genre(ugenre)
                books.set_quantity(uquantity)
                books.set_price(uprice)

                bm = booksModel(app)
                bm.update_book(books, ubid)

                flash("Book Updated Successfully", "info")
                return redirect("/")

    def books_available(self):
        return render_template("books_available.html")

    def check_book_availability(self):
        empty = 0
        text = "Book Not Exist"
        if request.method == "GET":
            tocheck = request.args.get("bookid")
            bm = booksModel(app)
            bquant = bm.book_available(tocheck)
            if len(bquant) == 0:
                return json.dumps(text)
            elif bquant[0][0] == 0:
                return json.dumps(empty)
            else:
                return json.dumps(bquant) #pass data to javascript

    def check_book_avail_by_name(self):
        empty = 0
        text = "Book Not Exist"
        if request.method == "GET":
            tocheck = request.args.get("bkname")
            print(tocheck)
            bm = booksModel(app)
            bquant = bm.book_available(tocheck)
            if len(bquant) == 0:
                return json.dumps(text)
            elif bquant[0][0] == 0:
                return json.dumps(empty)
            else:
                return json.dumps(bquant)

    def export_file(self):
        return render_template("export_file.html")

    def pdf_generator(self):
        return render_template("pdf_generator.html")

    def show_customer_actions(self):
        return render_template("customer_dashboard.html")