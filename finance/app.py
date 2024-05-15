import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    # TODO: what is the current price for each stock [DONE]
    # NOTE: return only the ones that havent been sold completely [HAVING]
    stocks = db.execute("SELECT symbol, SUM(quantity) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING shares <> 0", session["user_id"])
    for index, stock in enumerate(stocks):
        # look up the current price of the stock
        price = lookup(stock["symbol"])["price"]
        # calculate the worth of my stock shares
        total = price * stock["shares"]
        # update dictionary with current market values
        stocks[index]["price"] = price
        stocks[index]["total"] = total

    # how much does the user have
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    # get the grand total of all the transactions and the cash I have
    total = cash
    for stock in stocks:
        total += stock["total"]
    return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # shares must be a whole number
        try:
            shares = int(shares)
        except ValueError:
            return apology("Invalid shares")

        if not symbol:
            return apology("Enter symbol")
        elif not shares:
            return apology("Enter shares")
        elif shares < 0:
            return apology("Enter positive number")

        # how much is the shares you qant to buy
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol")

        # how much do you have
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]

        # can you afford to buy
        quantity = float(quote["price"]) * shares
        if quantity > cash:
            return apology("You cant afford that")

        # make the purchase since you can afford
        # log the purchase
        db.execute("INSERT INTO transactions (user_id, symbol, quantity, price, transaction_type) VALUES (?, ?, ?, ?, ?)", session["user_id"], quote["symbol"], shares, quote["price"], "buy")
        # update the amount of money you have
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", quantity, session["user_id"])
        # redirect to porfolio page after
        return redirect("/")


    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    records = db.execute("SELECT symbol, quantity AS shares, price, transaction_date FROM transactions WHERE user_id = ?", session["user_id"])
    return render_template("history.html", records=records)


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
        # NOTE: Lukhanyo and LuKhAnYo and lukhanyo, should be the same user
        # so I just sent them to lower
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username").lower()
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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
    quote = None
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Enter symbol")

        quote = lookup(symbol)
        if not quote:
            return apology("Invalid symbol")

    # render quote page
    return render_template("quote.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # grab form values
        username = request.form.get("username").lower()
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # validate fields to check if they are not empty
        if not username:
            return apology("Enter username")
        elif not password:
            return apology("Enter password")
        elif not confirmation:
            return apology("Enter password confirmation")

        # check if password and confirmation match
        if password != confirmation:
            return apology("Password do not match")

        # database commands below
        # check if username not already taken
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 0:
            return apology("Username already taken")

        # passwords match and username is available so lets register the user
        hash = generate_password_hash(password) # never store plain text password in database [security]
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        # send the user to the login page
        return redirect("/login")

    # render the regisrt page
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # NOTE: Complete the implementation of sell in such a way that it enables a user to sell shares of a stock (that he or she owns).
    # TODO: get all the stock shares of the user
    stocks = db.execute("SELECT symbol, SUM(quantity) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING shares <> 0", session["user_id"])
    # TODO: get the stock symbols that the user has bought [will show select menu with only the symbols he or she owns]
    symbols = [stock["symbol"] for stock in stocks]

    if request.method == "POST":
        # what is the user trying to sell and how much
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # TODO: you cant sell if you dont have anything
        if not symbol:
            return apology("What are you trying to sell")
        # TODO: how much are you selling
        elif not shares:
            return apology("How many shares are you selling")

        # NOTE: shares can only be a whole number
        try:
            shares = int(shares)
        except ValueError:
            return apology("Invalid shares")

        # TODO: do you really have how much you are trying to sell
        # dont bother querying the database again
        for stock in stocks:
            print(f"stock: {stock}")
            # check if the symbol match
            if stock["symbol"] == symbol and int(shares) > int(stock["shares"]):
                # you cant sell over
                return apology("You cant sell more than you own")
            elif stock["symbol"] == symbol and int(shares) <= int(stock["shares"]):
                # TODO: sell the stock
                # update the users money
                current_price = lookup(symbol)["price"]
                sold = float(current_price) * int(shares)
                db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", sold, session["user_id"])
                # keep record of what was sold
                db.execute("INSERT INTO transactions (user_id, symbol, quantity, price, transaction_type) VALUES (?, ?, ?, ?, ?)", session["user_id"], symbol, (-1 * int(shares)), current_price, "sell")
                # go to portfolio after selling the stock
                return redirect("/")

    return render_template("sell.html", symbols=symbols)

# PERSONAL TOUCH
@app.route("/profile")
@login_required
def profile():
    """Show user profile"""
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    return render_template("profile.html", cash=cash)

@app.route("/deposit", methods=["POST"])
@login_required
def deposit():
    """Deposit money to the user account"""
    amount = request.form.get("amount")

    if not amount:
        return apology("How much do you want to deposit")
    try:
        amount = float(amount)
    except ValueError:
        return apology("Invalid amount")

    if amount < 0:
        return apology("You cant deposit a negative amount")

    # deposit the money
    db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", amount, session["user_id"])
    return redirect("/profile")
