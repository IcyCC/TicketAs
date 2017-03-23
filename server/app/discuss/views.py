from datetime import datetime
from flask import render_template,session,redirect,url_for,request,jsonify
from . import discuss
from .. import *
from ..models import User,Post
from flask_login import login_user,logout_user,login_required,current_user


@discuss.route("/post",methods=['GET','POST','DELETE'])
@login_required
def api_post():
    user = User.query.filter_by(id=current_user.get_id()).first()
    if request.method == 'GET':
        user_id= request.args.get("id")
        if user_id is None:
            posts = Post.query.all()
            print posts
            return jsonify(status="success", posts=[p.to_json() for p in posts])
        else:
            posts = Post.query.filter_by(user_id=user_id).all()
            return jsonify(status="success", posts=[p.to_json() for p in posts])
    if request.method == 'POST':
        tittle = request.form.get("tittle")
        body = request.form.get("body")
        db.session.add(Post(tittle=tittle, body=body, user=user))
        db.session.commit()
        return jsonify(status="success")
    if request.method == 'DELETE':
        post_id = request.args.get("post_id")
        db.session.delete(Post.query.filter_by(id=post_id).first())
        db.session.commit()
        return jsonify(status="success")