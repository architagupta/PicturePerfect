from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "customer"
    username = db.Column(db.String(120), primary_key=True)
    email = db.Column(db.String(120))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    password = db.Column(db.String(54))
    confirmed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self,username, firstname, lastname, email, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.set_password(password)
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<username %r>' % self.password

class PremiumCustomer(db.Model):
    __tablename__ = "premiumcustomer"
    premiumid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120),db.ForeignKey('customer.username'))
    paymentstatus = db.Column(db.String(120),default="NULL")
    ispremium = db.Column(db.Boolean, default=False, nullable=False)
    paymentid = db.Column(db.String(100),default="NULL")

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return '<username %r>' % self.password
