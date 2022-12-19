from flask import Flask
from flask import render_template
from dotenv import load_dotenv

# 環境変数を上書き
load_dotenv(override=True)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('form.html')