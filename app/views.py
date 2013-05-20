from app import app
from flask import render_template, url_for, redirect, flash, request

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#@app.before_request

#@app.after_request

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
