from market import db, app, login_manager
from market import bcrypt
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    balance = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_balance(self):
        if len(str(self.balance)) >= 4:
            return f'{str(self.balance)[:-3]},{str(self.balance)[-3:]}$'
        else:
            return f"{self.balance}$"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def can_purchase(self, item_obj):
        return self.balance >= item_obj.price

    def can_sell(self, item_obj):
        return item_obj in self.items or item_obj in self.items2 or item_obj in self.items3 or item_obj in self.items4

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def buy(self, user):
        self.owner_id = user.id
        user.balance -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner_id = None
        user.balance += self.price
        db.session.commit()


class Item2(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    owner = db.relationship("User", backref="items2")

    def buy(self, user):
        self.owner_id = user.id
        user.balance -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner_id = None
        self.owner = None
        user.balance += self.price
        db.session.commit()


class Item3(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    owner = db.relationship("User", backref="items3")

    def buy(self, user):
        self.owner_id = user.id
        user.balance -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner_id = None
        self.owner = None
        user.balance += self.price
        db.session.commit()

class Item4(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    owner = db.relationship("User", backref="items4")

    def buy(self, user):
        self.owner_id = user.id
        user.balance -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner_id = None
        self.owner = None
        user.balance += self.price
        db.session.commit()

with app.app_context():
    db.create_all()
