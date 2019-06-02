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
from forms.forms import registration, loginForm, addModel
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

@app.before_request
def before_request():
        g.username = None
        if 'username' in session:
                g.username = session['username']
        if 'search' in session:
                g.search = session['search']

@app.route("/")
@app.route("/Home")
@app.route("/home")
def home():
        if g.username:
                username=g.username
                return redirect(url_for('adminDash', username=username))
        else:
                return render_template('index.html')

@app.route('/register/', methods=["GET","POST"])
def register():
        if g.username:
                username=g.username
                return render_template('adminDash.html', username=username)
        else:
                form = registration(request.form)
                if request.method == 'POST':
                        pw_hash =bcrypt.generate_password_hash(form.password.data)
                        newEntry = [((form.username.data), pw_hash, (form.emailAddress.data))]
                        conn =sqlite3.connect('static/user_db.db')
                        print ("Opened database successfully")
                        with conn:
                                c =conn.cursor()
                                try:
                                        sql = '''INSERT INTO user (username, password, email) VALUES(?,?,?)'''
                                        conn.executemany(sql, newEntry)
                                        print ("Insert correctly")
                                except:
                                        flash("This is already an account, please log in with those details or change details.")
                                        return render_template("register.html", form=form)
                                        conn.commit()

                                flash((form.username.data) + " Successfully Registered!")
                                return redirect('login')
                        return render_template("register.html", form=form)
                return render_template("register.html", form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
        form = loginForm(request.form)       
        if request.method == 'POST':  
                conn = sqlite3.connect('static/user_db.db')
                
                with conn:
                        c = conn.cursor()
                        find_user = ("SELECT * FROM user WHERE username = ?")
                        c.execute(find_user, [(form.username.data)])  
                        results =c.fetchall()
                        
                        userResults = results[0]
                        print(userResults)
                        print(form.password.data)
                        if bcrypt.check_password_hash(userResults[1],(form.password.data)):
                                session['logged_in'] = True
                                session['username'] = (form.username.data)
                                return redirect(url_for('adminDash'))
                        else:
                                flash('Either username or password was not recognised')
                                return render_template('login.html', form=form) 

                                 
                return render_template("login.html", form=form)
        
        return render_template("login.html", form=form)

@app.route("/logout")
def logout():        
        session['logged_in'] = True
        session.clear()
        flash("You have successfully logged out.")
        return render_template("index.html")


@app.route('/adminDash/')
def adminDash():
        if g.username:
                username=g.username
                return render_template('adminDash.html', username=username)
        else:
                flash('Please Login to continue')
                return redirect('login')

@app.route('/addEntry/')
def addEntry():
        form = addModel(request.form)
        return render_template('addEntry.html', form=form)

@app.route('/deleteEntry/')
def deleteEntry():
        return render_template('deleteEntry.html')

if __name__ == "__main__":
      app.run('localhost', 5000, debug=True)