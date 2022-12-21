from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from mail import send_mail
from datetime import datetime
from log import make_log_dir, write_log

# 環境変数を上書き
load_dotenv(override=True)
app = Flask(__name__)

# データベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# データベースの初期化
db = SQLAlchemy(app)

# テーブルの定義
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    substance = db.Column(db.String, nullable=False)
    send_email = db.Column(db.Boolean, nullable=False)

# エラー対応 アプリケーションコンテキストの複数回参照について
with app.app_context():
    file_path = '/instance/contacts.db'
    # もしもデータベースが作成されていない場合、作成を行う
    if not os.path.exists(file_path):
        db.create_all()

# ホーム画面
@app.route('/', methods=['GET', 'POST'])
def home():
    # GET(アクセス)の場合
    if request.method == 'GET':
        contacts = Contact.query.all()
        return render_template('index.html', posts=contacts)
    # POST(問い合わせの送信)の場合
    else:
        name = request.form.get('contacter_name')
        email = request.form.get('contacter_email')
        title = request.form.get('contacter_title')
        substance = request.form.get('contacter_substance')
        sended = True
        try:
            send_mail()
        except:
            sended = False
            now = str(datetime.now())
            make_log_dir()
            write_log(now + ": undefine error")
        finally:
            post = Contact(name=name, email=email, title=title, substance=substance, send_email=sended)
            db.session.add(post)
            db.session.commit()
            return redirect('/')

# 問い合わせ画面
@app.route('/contact')
def contact():
    return render_template('form.html')