"""
 Copyright (c) 2022, Ricardo Madeira
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.  
"""

import os

import re
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

app.jinja_env.globals.update(usd=usd)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    portfolio = db.execute("SELECT * FROM portfolios WHERE user_id = ?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    total = 0 + cash

    for stock in portfolio:
        stock["price"] = lookup(stock["symbol"])["price"]
        stock["total"] = stock["price"] * stock["shares"]
        total += stock["total"]
        stock["price"], stock["total"] = usd(stock["price"]), usd(stock["total"])

    return render_template("index.html", portfolio=portfolio, cash=usd(cash), total=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        quote_result = lookup(symbol)

        # Check if shares and quotes are ok
        if quote_result == None:
            return apology(f"Can't find {symbol}!")
        if not symbol:
            return apology(f"No symbol was provided!")
        if not shares:
            return apology(f"No amount of shares provided!")

        # Check if input of shares is integer
        if not re.search("^\d+$", shares):
            return apology(f"Invalid value for shares!")

        shares = int(shares)
        price = quote_result["price"]
        user = session["user_id"]
        company = quote_result["name"]

        # Check if sufficient funds
        if db.execute("SELECT cash FROM users WHERE id = ?", user)[0]["cash"] < (price * shares):
            return apology("Insufficient funds")

        # Update funds after buying
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", (price * shares), user)

        # Create transaction in database
        db.execute("INSERT INTO transactions (user_id, stock_symbol, price, shares, total_price, type_transaction) VALUES (?, ?, ?, ?, ?, ?)",
                   user, symbol, price, shares, price * shares, "buy")

        # If user doesn't have the stock yet we have to add it to portfolio
        if not db.execute("SELECT * FROM portfolios WHERE user_id = ? AND symbol = ?", user, symbol):
            db.execute("INSERT INTO portfolios (user_id, symbol, company, shares) VALUES (?, ?, ?, ?)", user, symbol, company, shares)

        # Else we just update the shares
        else:
            db.execute("UPDATE portfolios SET shares = shares + ? WHERE user_id = ? AND symbol = ?", shares, user, symbol)

        # To send an alert in the main page
        flash("Bought!")

        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        print(session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        quote_result = lookup(symbol)

        if quote_result == None:
            return apology(f"Can't find {symbol}!")

        if not symbol:
            return apology(f"No symbol was provided!")

        return render_template("quote_result.html", quote_result=quote_result)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("You didn't provide a username")
        if not password:
            return apology("You didn't provide a password")
        if db.execute("SELECT username FROM users WHERE username = ?", username):
            return apology("Username already in use")
        if not confirmation or confirmation != password:
            return apology("Password confirmation doesn't match the password you provided")

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        session["user_id"] = db.execute("SELECT id FROM users WHERE username=?", username)[0]["id"]
        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        user = session["user_id"]
        quote_result = lookup(symbol)

        if not re.search("^\d+$", shares):
            return apology(f"Invalid value for shares!")

        shares = int(shares)

        if quote_result == None:
            return apology(f"Can't find {symbol}!")
        if not symbol:
            return apology(f"No symbol was provided!")
        if not shares:
            return apology(f"No amount of shares provided!")
        if db.execute("SELECT * FROM portfolios WHERE user_id = ? AND symbol = ?", user, symbol)[0]["shares"] < shares:
            return apology(f"You don't own enough shares of {symbol}")
        if not db.execute("SELECT * FROM portfolios WHERE user_id = ? AND symbol = ?", user, symbol)[0]["shares"]:
            return apology(f"You don't own shares of {symbol}")

        price = quote_result["price"]

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", (price * shares), user)

        db.execute("UPDATE portfolios SET shares = shares - ? WHERE user_id = ? AND symbol = ?", shares, user, symbol)

        flash("Sold!")

        return redirect("/")

    symbols = db.execute("SELECT symbol FROM portfolios WHERE user_id = ?", session["user_id"])
    return render_template("sell.html", symbols=symbols)
