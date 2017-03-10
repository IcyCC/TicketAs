#coding=utf-8
from datetime import datetime
from flask import render_template,session,redirect,url_for,request,jsonify
from . import main
from .forms import*
from .. import *


@main.route('/',methods = ['GET',])
def index():
    return render_template('index.html')
