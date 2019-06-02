from flask import Flask, render_template, request, redirect, Response, url_for, session, abort, g, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
import hashlib
from config import Config
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect, CSRFError
from forms.forms import registration, loginForm
import sqlite3

app = Flask(__name__)
bcrypt = Bcrypt(app)
LoginManager = LoginManager(app)
app.config['SESSION_TYPE'] = 'filesystem'
photos = UploadSet('photos')
app.config['UPLOADED_PHOTOS_DEST']= 'static'
configure_uploads(app, photos)
mysql = MySQL()
mysql.init_app(app)
app.config.from_object(Config)
csrf = CSRFProtect(app)

@app.route("/")
def home():
        return render_template('index.html')

@app.route('/register/', methods=["GET","POST"])
def register():
        form = registration(request.form)
        if request.method == 'POST':
                pw_hash =bcrypt.generate_password_hash(form.password.data)
                newEntry = [((form.username.data), pw_hash, (form.emailAddress.data))]
                conn =sqlite3.connect('static/user_db.db')
                print ("Opened database successfully")
                completion = False
                with conn:
                        c =conn.cursor()
                        try:
                                sql = '''INSERT INTO users (username, password, email) VALUES(?,?,?)'''
                                conn.executemany(sql, newEntry)
                                print ("TAble created successfully")
                        except:
                                error ="This is already an account, please log in with those details or change details."
                                return render_template("register.html", error=error)
                                conn.commit()

                        flash((form.username.data) + " Successfully Registered!")
                        return render_template("login.html", form=form)
                return render_template("register.html", form=form)
        return render_template("register.html", form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
        form = loginForm(request.form)
        if request.method == 'POST':                
                return render_template("login.html", form=form)
        
        return render_template("login.html", form=form)

if __name__ == "__main__":
      app.run('localhost', 5000, debug=True)