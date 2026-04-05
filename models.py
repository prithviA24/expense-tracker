 
from flask_sqlalchemy import SQLAlchemy

# create the database object
# we'll connect it to the Flask app in app.py
db = SQLAlchemy()

class Expense(db.Model):
    # each attribute = one column in the database table

    id = db.Column(db.Integer, primary_key=True)
    # primary_key=True means this is the unique ID for each row
    # auto increments — 1, 2, 3, 4...

    name = db.Column(db.String(100), nullable=False)
    # name of the expense e.g. "Lunch", "Uber"
    # nullable=False means this field is required

    amount = db.Column(db.Float, nullable=False)
    # amount spent e.g. 150.00

    category = db.Column(db.String(50), nullable=False)
    # category e.g. "Food", "Transport", "Shopping"

    date = db.Column(db.String(20), nullable=False)
    # date as a string e.g. "2024-01-15"

    def __repr__(self):
        # this is what prints when you do print(expense)
        return f"<Expense {self.name} - {self.amount}>"