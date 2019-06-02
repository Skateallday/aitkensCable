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
from forms.forms import registration

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registration(request.form)
    if request.method == 'POST' and form.validate():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(form.username.data, form.email.data,
                     pw_hash)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
        error = None
        if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                con = mysql.get_db("aitkenscable_equipment.sql").cursor()
                completion = False
                with con:
                        c = con.cursor()
                        find_user = ("SELECT * FROM USER WHERE USERNAME = ? ")
                        c.execute(find_user, [(username)])
                        results = c.fetchall()                  
                        try:
                                userResults = results[0]
                                results and bcrypt.check_password_hash(userResults[2], password) 
                                session['logged_in'] = True
                                session['username'] = username
                                return redirect(url_for('homepage'))
                        except Exception:
                                error=("username and password not recognised")
                                return render_template('login.html', error=error)
        
        return render_template('login.html')

if __name__ == "__main__":
      app.run('localhost', 5000, debug=True)