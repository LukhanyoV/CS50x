import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        id = request.form.get("id")
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # post for new data
        if not id:
            # make sure all fields are not empty before sending to the database
            if name and month and day:
                db.execute("INSERT INTO birthdays(name, month, day) VALUES(?, ?, ?);", name, month, day)
        # post for existing data
        else:
            # make sure all fields are filled in before updating
            if name and month and day and id:
                db.execute("UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?", name, month, day, id)

        # redirect back to home
        return redirect("/")

    else:
        # TODO: get the record to be updated by id
        id = request.args.get("id")
        human = db.execute("SELECT * FROM birthdays WHERE id = ?", id)
        if human:
            human = human[0]
        button = "Update" if id else "Add"

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays;")

        return render_template("index.html", birthdays=birthdays, human=human, id=id, button=button)


# optional delete birthday entry
@app.route("/delete", methods=["POST"])
def delete():

    # TODO: Delete user birthday
    id = request.form.get("id")

    # make sure you got the id
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?;", id)

    return redirect("/")

