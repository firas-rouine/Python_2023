from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.user import User
from flask_app.models.appointment import Appointment
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/appointments')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_appointments = Appointment.get_user_appointments({'user_id':session['user_id']})
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html",user=logged_user, appointments=all_appointments)



@app.route("/users/register" , methods=['POST'])
def user_register():
    if not User.validate(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : pw_hash
    }
    user_id = User.create(data)
    
    session["user_id"]=user_id
    alert_message = "Creating successful."
    return render_template('index.html', alert_message=alert_message)


@app.route("/users/login" , methods=['POST'])
def login():
    data ={
        "email" : request.form['email']
    }

    user_in_db =User.get_by_email(data)
    if not user_in_db :
        flash("invalid credentials" ,"log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password , request.form['password']):
        flash("invalid credentials" ,"log")
        return redirect("/")
    session['user_id']=user_in_db.id
    return redirect("/appointments")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')