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
from forms.forms import registration, loginForm, addModel, forgotPassword, PasswordForm, viewItems, editModel
import sqlite3
from itsdangerous import URLSafeTimedSerializer

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
table =""

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
                return render_template('adminDash.html', username=g.username)
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
                                        c.executemany(sql, newEntry)
                                        print ("Insert correctly")
                                except:
                                        flash("This is already an account, please log in with those details or change details.")
                                        return render_template("register.html", form=form)
                                        c.commit()

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


@app.route('/adminDash/', methods=['GET', 'POST'])
def adminDash():
        if g.username:
                
                return render_template('adminDash.html')
        else:
                flash('Please Login to continue')
                return redirect('login')

@app.route('/editEntry/<data>', methods=['GET', 'POST'])
def editEntry(data):
        if g.username:
                form= editModel(request.form)
                conn = sqlite3.connect('static/data.sqlite')
                        
                c = conn.cursor()
                print(data)     
                print([data])                                   
                c.execute('SELECT * FROM items WHERE model_number LIKE (?)', (data,))
                results = c.fetchall()
                if results:
                        for result in results:
                                print(results)
                                print(result)
                                error="Change the form as you please"
                                return render_template('editEntry.html', error=error, data=result, form=form)
                else:
                        error="Something has gone wrong"
                        return render_template('editEntry.html', form=form, error=error)
        
        else:
                flash('Please Login to continue')
                return redirect('login')
        

@app.route('/viewItem/', methods=['GET', 'POST'])
def viewItem():
        if g.username:
                error=""
                form= viewItems(request.form)
                if request.method == 'POST':
                        table = form.itemCategory.data
                        print(table)
                        conn = sqlite3.connect('static/data.sqlite')
                        
                        c = conn.cursor()
                                                                                        
                        search=('''SELECT * FROM items WHERE item_category LIKE (?)''')
                        c.execute(search, [table])
                        rows = c.fetchall()
                        if rows:

                                for row in rows:
                                        print(row)
                                        print(rows)
                                        results = rows
                                        return render_template('viewItems.html', results=results, form=form)
                        else:
                                error="Sorry there are no results"
                                return render_template('viewItems.html', error=error, form=form)

                else:
                        error=""
                        return render_template('viewItems.html', error=error, form=form)
        else:
                flash('Please Login to continue')
                return redirect('login')


@app.route('/addEntry/', methods=['GET', 'POST'])
def addEntry():
        if g.username:
                form = addModel(request.form)

                if request.method == 'POST':   
                        table=(form.itemCategory.data)                     
                        item_name =(form.itemName.data)
                        print(item_name)
                        item_Ref =(form.modelRef.data)
                        print(item_Ref)
                        model_number =(form.modelNumber.data)
                        item_category =(form.itemCategory.data)
                        measurement1=(form.measurements.data)
                        value1=(form.value.data)
                        measurement2=(form.measurements2.data)
                        value2=(form.value2.data)
                        measurement3=(form.measurements3.data)
                        value3=(form.value3.data)
                        measurement4=(form.measurements4.data)
                        value4=(form.value4.data)
                        entry=[(item_name, item_Ref, model_number, item_category, measurement1, value1, measurement2, value2, measurement3, value3, measurement4, value4)]
                        print(entry)                             
                        print(table)

                        conn = sqlite3.connect('static/data.sqlite')                
                        with conn:
                                c = conn.cursor()
                                try:
                                        insert_into = '''INSERT INTO items (item_name, model_number, model_ref, item_category,  measurement1, value1, measurement2, value2, measurement3, value3, measurement4, value4 ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''                      
                                        conn.executemany(insert_into, entry)
                                        message = "You have added " + item_name + " to the database."
                                        flash(message)
                                        return redirect(url_for('adminDash'))
                                except Exception as e: print(e)
                        return render_template('addEntry.html', form=form)                                        
                else:
                        return render_template('addEntry.html', form=form)
        return render_template('addEntry.html', form=form)





@app.route('/reset/', methods=['GET', 'POST'])
def forgotpassword():
        form = forgotPassword(request.form)
        if form.validate_on_submit():
                conn = sqlite3.connect('static/user_db.db')
                
                with conn:
                        c = conn.cursor()
                        find_user = ("SELECT * FROM user WHERE email = ?")
                        c.execute(find_user, [(form.email.data)])  
                        user =c.fetchall()
                        fuser = user[0]
                        find_email = ("SELECT  email FROM user")
                        c.execute(find_email)
                        email =c.fetchall()
                        Femail = email[0]
                        print(fuser[2])
                        print(Femail[0])

                
                if fuser[2] == Femail[0]:
                        send_password_reset_email(Femail[0])
                        flash('Please check your email for a password reset link.', 'success')
                else:
                        flash('Your email address must be confirmed before attempting a password reset.', 'error')
        return render_template('forgotPassword.html', form=form)

def send_password_reset_email(user_email):
    password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
 
    password_reset_url = url_for(
        'reset_with_token',
        token = password_reset_serializer.dumps(user_email, salt='password-reset-salt'),
        _external=True)
 
    html = render_template(
        'email_password_reset.html',
        password_reset_url=password_reset_url)
 
    send_email('Password Reset Requested', [user_email], html)


@app.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    try:
        password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = password_reset_serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except:
        flash('The password reset link is invalid or has expired.', 'error')
        return redirect(url_for('users.login'))
 
    form = PasswordForm()
 
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=email).first_or_404()
        except:
            flash('Invalid email address!', 'error')
            return redirect(url_for('users.login'))
 
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('users.login'))
 
    return render_template('reset_password_with_token.html', form=form, token=token)

@app.route('/deleteEntry/')
def deleteEntry():
        return render_template('deleteEntry.html')

if __name__ == "__main__":
      app.run('localhost', 5000, debug=True)