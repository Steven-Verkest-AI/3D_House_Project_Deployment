from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#https://www.youtube.com/watch?v=KrRzZGcHjK8
#https://www.youtube.com/watch?v=w25ea_I89iM

#trying to acces the sqlite database with sqlalchemy code

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////C://Users//Steven Verkest//CSV_TIF_test1.db"
db = SQLAlchemy(app)

class ExampleTable(db.Model):
    __tablename__='tile_12040'
    id = db.Column(db.Integer,primary_key=True)
    


db.create_all()
