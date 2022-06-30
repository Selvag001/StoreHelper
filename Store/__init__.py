from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os



app = Flask(__name__)
app.config['SECRET_KEY']='mysecret'

#Database information
data_dir_path = 'sqlite:///'+(os.path.abspath(os.path.join(os.path.curdir,'data/db.sqllite'))).replace('\\','/')
#print(data_dir_path)
app.config['SQLALCHEMY_DATABASE_URI']=data_dir_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
migrate=Migrate(app,db)


from Store.Product.views import product
app.register_blueprint(product,url_prefix='/product')

@app.route('/')
def index():
    return redirect(url_for('Product.catalog'))





