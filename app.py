import jinja2
from flask import Flask, request, redirect, render_template, url_for


app = Flask(__name__)

@app.route('/')
def page():
    """Display the web page."""
    return render_template('/index.html')

@app.route('/base')
def base():
    """basehtml"""
    return render_template('/base.html')

@app.route('/charities.html')
def charity():
    """charities page"""
    return render_template('/charities.html')


if __name__ == '__main__':
    app.run(debug=True)