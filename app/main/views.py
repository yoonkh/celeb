from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries

from app.press import sports_dong_a
from . import main


@main.route('/')
def index():
    return '<marquee><h1>Success</h1></marquee>'


@main.route('/crawl')
def crawl():
    sports_dong_a.main()
    return '<marquee><h1>Success - Crawling</h1></marquee>'