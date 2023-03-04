from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, Item2, Item3, Item4, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/products")
@login_required
def products():
    return render_template("products.html")


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category="success")
        return redirect(url_for('products'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category='danger')
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('products'))
        else:
            flash('Username and password are incorrect! Please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))


@app.route("/laptops", methods=['GET', 'POST'])
def laptops():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately you don't have enough money to purchase {p_item_object.name}", category='danger')
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to market ",
                      category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name} ", category='danger')

        return redirect(url_for('laptops'))

    if request.method == "GET":
        items = Item.query.filter_by(owner_id=None)
        owned_items = Item.query.filter_by(owner_id=current_user.id)
        return render_template("laptops.html", items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)


@app.route("/smartphones", methods=['GET', 'POST'])
def smartphones():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        purchased_item2 = request.form.get('purchased_item2')
        p_item_object = Item2.query.filter_by(name=purchased_item2).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately you don't have enough money to purchase {p_item_object.name}", category='danger')
        sold_item2 = request.form.get('sold_item2')
        s_item_object = Item2.query.filter_by(name=sold_item2).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to market ",
                      category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name} ", category='danger')


        return redirect(url_for('smartphones'))

    if request.method == "GET":
        items = Item2.query.filter_by(owner_id=None)
        owned_items2 = Item2.query.filter_by(owner_id=current_user.id)
        return render_template("smartphones.html", items=items, purchase_form=purchase_form, owned_items2=owned_items2, selling_form=selling_form)


@app.route("/tv", methods=['GET', 'POST'])
def tv():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        purchased_item4 = request.form.get('purchased_item4')
        p_item_object = Item4.query.filter_by(name=purchased_item4).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately you don't have enough money to purchase {p_item_object.name}", category='danger')
        sold_item4 = request.form.get('sold_item4')
        s_item_object = Item4.query.filter_by(name=sold_item4).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to market ",
                      category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name} ", category='danger')

        return redirect(url_for('tv'))

    if request.method == "GET":
        items = Item4.query.filter_by(owner_id=None)
        owned_items4 = Item4.query.filter_by(owner_id=current_user.id)
        return render_template("tv.html", items=items, purchase_form=purchase_form, owned_items4=owned_items4, selling_form=selling_form)


@app.route("/tablets", methods=['GET', 'POST'])
def tablets():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        purchased_item3 = request.form.get('purchased_item3')
        p_item_object = Item3.query.filter_by(name=purchased_item3).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately you don't have enough money to purchase {p_item_object.name}", category='danger')
        sold_item3 = request.form.get('sold_item3')
        s_item_object = Item3.query.filter_by(name=sold_item3).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to market ",
                      category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name} ", category='danger')
        return redirect(url_for('tablets'))

    if request.method == "GET":
        items = Item3.query.filter_by(owner_id=None)
        owned_items3 = Item3.query.filter_by(owner_id=current_user.id)
        return render_template("tablets.html", items=items, purchase_form=purchase_form, owned_items3=owned_items3, selling_form=selling_form)
