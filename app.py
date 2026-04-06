 
from flask import Flask, render_template, request, redirect, url_for
from models import db, Expense
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

app = Flask(__name__)

# database configuration
# SQLite file will be created automatically as expenses.db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "devkey123")

# connect database to app
db.init_app(app)

# create tables if they don't exist
with app.app_context():
    db.create_all()

# ─── ROUTES ───────────────────────────────────────────

@app.route("/")
def index():
    # fetch all expenses from database, newest first
    expenses = Expense.query.order_by(Expense.id.desc()).all()

    # calculate total
    total = sum(e.amount for e in expenses)

    return render_template("index.html", expenses=expenses, total=total)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # get form data
        name = request.form.get("name")
        amount = float(request.form.get("amount"))
        category = request.form.get("category")
        date = request.form.get("date")

        # create new expense object
        expense = Expense(name=name, amount=amount,
                         category=category, date=date)

        # save to database
        db.session.add(expense)
        db.session.commit()

        # redirect back to home page
        return redirect(url_for("index"))

    # GET request — just show the form
    today = datetime.today().strftime("%Y-%m-%d")
    return render_template("add.html", today=today)


@app.route("/delete/<int:id>")
def delete(id):
    # find expense by id
    expense = Expense.query.get_or_404(id)

    # delete it
    db.session.delete(expense)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)