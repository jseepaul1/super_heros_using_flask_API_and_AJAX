from flask_app import app
from flask import render_template, redirect, request, session, jsonify
import os
import requests

from flask_app.models.superhero import Superhero


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/searching', methods=['POST'])
def search():
    r = requests.get(
        f"https://superheroapi.com/api/{os.environ.get('SUPER_HERO_API_KEY')}/search/{request.form['query']}")
    return jsonify(r.json())
