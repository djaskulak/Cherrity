import jinja2
from flask import Flask, request, redirect, render_template, url_for


app = Flask(__name__, template_folder="templates")

@app.route('/')
def page():
    """Display the web page."""
    return render_template('index.html')

@app.route('/base')
def base():
    """basehtml"""
    return render_template('base.html')

@app.route('/charities')
def charity():
    """charities page"""
    return render_template('charities.html')

@app.route('/resources')
def resources():
    """resources page"""
    return render_template('resources.html')

@app.route('/blog')
def blog():
    """blog page"""
    return render_template('blog.html')

@app.route('/cart')
def cart():
    """cart html"""
    return render_template('cart.html')



if __name__ == '__main__':
    app.run(debug=True)