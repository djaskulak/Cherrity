import jinja2
from flask import Flask, request, redirect, render_template, url_for
import matplotlib
import matplotlib.pyplot as plt
import os
import pytz
import requests
import sqlite3

from pprint import PrettyPrinter
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


app = Flask(__name__, template_folder="templates")

load_dotenv()
API_KEY = os.getenv('API_KEY')
pp = PrettyPrinter(indent=4)
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
    charity_search = request.args.get('charitysearch')
    url = 'https://api.data.charitynavigator.org/v2/Organizations?'

    params = {

        'app_id': '8f2c6d67',
        'app_key': 'e5e5bdc2fdb7f36e504cc8478d9f88fe',
        'search': charity_search

    }

    result_json = requests.get(url, params=params).json()
    pp.pprint(result_json)
    context = {
        'name': result_json[0]['charityName'],
        'ein': result_json[0]['ein'],
        'rating': result_json[0]['charityNavigatorURL']


    }

    return render_template('charities.html', **context)

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