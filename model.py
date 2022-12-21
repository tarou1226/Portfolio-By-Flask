from flask_sqlalchemy import SQLAlchemy
from main import app

# データベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True

# データベースの初期化
db = SQLAlchemy(app)

# テーブルの定義
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    substance = db.Column(db.String, nullable=False)

# エラー対応 アプリケーションコンテキストの複数回参照について
with app.app_context():
    db.create_all()
