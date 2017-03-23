from .. import db
from datetime import datetime
from flask import render_template,session,redirect,url_for,request,jsonify,g
from flask_login import login_user,logout_user,login_required,current_user
from . import auth
from ..models import *


@auth.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        remeber_me = request.form.get("remeber_me")

        if remeber_me == 'false':
            remeber_me = False
        else:
            remeber_me = True

        user = User.query.filter_by(username=username).first()
        if user is None:
            return jsonify(status="fail", reason="No this user")
        else:
            if user.verify_password(password):
                print type(remeber_me)
                login_user(user, remeber_me)
                return jsonify(status="success", username=username)
            else:
                return jsonify(status="fail", reason="wrong  user")


@auth.route("/logout", methods=['GET',])
@login_required
def logout():
    logout_user()
    return jsonify(status="success")


@auth.route("/users", methods =['GET','POST','DELETE'])
def api_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify(status="success", users=[u.to_json() for u in users])
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db.session.add(User(username=username, password = password))
        db.session.commit()
        return jsonify(status="success",users=username)
    if request.method == 'DELETE':
        username = request.args.get("username")
        user = User.query.filter_by(username=username).first()
        if user is None:
            return jsonify(status="fail")
        else:
            db.session.delete(user)
            return jsonify(status="success")

@auth.route("/current",methods=['GET',])
def api_getcurrent():
    if current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.get_id()).first()
        return jsonify(status="success", is_login=True, user=user.to_json())
    else:
        return jsonify(status="fail", is_login=False)