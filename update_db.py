from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus as urlquote

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:{}@106.15.196.160:3306/fcDataset'.format(urlquote("@nanxin11"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Info(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16))
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(16))
    addtime = db.Column(db.DATETIME,index=True,default=datetime.now)
    license = db.Column(db.Integer, default=0)
if __name__ == "__main__":
    db.drop_all()
    db.create_all()
