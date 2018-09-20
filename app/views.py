from flask import render_template, session, request, redirect, url_for, Response, make_response, abort
from app import app, db
from app.models import User
from app.utils.auth_utils import encode, decode
from flask_sqlalchemy import SQLAlchemy


@app.route("/")
@app.route("/index")
def index():
    user_cookie = request.cookies.get('username')

    if user_cookie is None:
        return redirect(url_for('login'), 302)

    username = decode(app.config['SECRET_KEY'], str(user_cookie))

    user = User.query.filter_by(username=username).first()

    if user is None:
        return redirect(url_for('login'), 302)

    return render_template('index.html')

@app.route("/login")
def login():
    user_cookie = request.cookies.get('username')

    if user_cookie is not None:
        username = decode(app.config['SECRET_KEY'], str(user_cookie))

        user = User.query.filter_by(username=username).first()

        if user is not None:
            return redirect(url_for('index'), 302)

    return render_template('login.html')


@app.route("/auth/login", methods=['POST'])
def login_user():
    data_dict = request.get_json()
    username = data_dict['username']
    # TODO: Compute hash and salt of passwords
    password = data_dict['password']

    user = User.query.filter_by(username=username, hashed_password=password).first()

    if (user is None):
        abort(404)

    # Generate cookie
    user_cookie = encode(app.config['SECRET_KEY'], user.username)

    res = make_response()
    res.set_cookie("username", value=user_cookie)

    # TODO: Properly return a 200 response
    return res


@app.route("/auth/register", methods=['POST'])
def register_user():
    # TODO: Server-side checks and sanitize inputs
    # TODO: Hash and salt passwords
    # TODO: Check for email/username duplication
    data_dict = request.get_json()
    username = data_dict['username']
    email = data_dict['email']
    password = data_dict['password']
    confirm_password = data_dict['confirm_password']

    new_user = User(username, email, password)
    db.session.add(new_user)
    db.session.commit()

    # TODO: Properly return a 200 response
    return make_response()
