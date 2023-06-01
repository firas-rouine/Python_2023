from flask_app import app
from flask_app.models.appointment import Appointment
from flask import request , redirect, session, render_template, flash


# ===========================DASHBOARD==================

@app.route('/appointments/add' )
def new_appointment():
    if 'user_id' not in session:
        return redirect('/') 
    return render_template("new_appointment.html") 

@app.route('/appointments/add', methods=['POST'])
def add_appointment():
    if 'user_id' not in session:
        return redirect('/') 
    if not Appointment.validate_appointment(request.form):
        return redirect("/appointments/add")
    data = {
        **request.form,
        'user_id': session["user_id"] 
    }
    Appointment.create_appointment(data)
    
    return redirect("/appointments")

@app.route('/appointments/<int:id>')
def edit_appointment(id):
    if 'user_id' not in session:
        return redirect('/') 
    appointment = Appointment.get_by_id({'id':id})
    return render_template("edit_appointment.html",  appointments = appointment)


@app.route('/appointments/<int:id>',methods=['post'])
def update_appointment(id):
    if not Appointment.validate_appointment(request.form):
        return redirect(f"/appointments/{id}")
    user=Appointment.update_appointment(request.form)
    print(user)
    return redirect('/appointments')

@app.route('/appointments/<int:id>/delete')
def delete_party(id):
    Appointment.delete_appointment({'id':id})
    return redirect('/appointments')



# # def all_parties():
# #     all_party=Party.get_all_parties()
# #     return render_template("my_parties.html",all_parties=all_party)
# @app.route('/my_parties')
# def my_parties():
#     user_parties = Party.get_user_parties({'user_id':session['user_id']})
#     logged_user = User.get_by_id({'id':session['user_id']})
#     return render_template("my_parties.html", parties = user_parties, user = logged_user)