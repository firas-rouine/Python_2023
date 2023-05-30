from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.party import Party
from flask import request , redirect, session, render_template, flash


# ===========================DASHBOARD==================
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_parties = Party.get_all_parties()
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", all_parties = all_parties, user = logged_user)
@app.route('/parties/new' )
def new_party():
    if 'user_id' not in session:
        return redirect('/') 
    return render_template("new_party.html") 

@app.route('/parties/create', methods=['POST'])
def add_party():
    if 'user_id' not in session:
        return redirect('/') 
    if not Party.validate_party(request.form):
        return redirect("/parties/new")
    data = {
        **request.form,
        'user_id': session["user_id"] 
    }
    Party.create_party(data)
    
    return redirect("/dashboard")

@app.route('/parties/<int:id>')
def show_party(id):
    if 'user_id' not in session:
        return redirect('/') 
    party = Party.get_by_id({'id':id})
    return render_template("show.html",  party = party)
@app.route('/parties/<int:id>/edit')
def edit_party(id):
    if 'user_id' not in session:
        return redirect('/') 
    party = Party.get_by_id({'id':id})
    return render_template("edit_party.html",  party = party)


@app.route('/parties/<int:id>/update',methods=['post'])
def update_party(id):
    if not Party.validate_party(request.form):
        return redirect(f"/parties/{id}/edit")
    Party.update_party(request.form)
    return redirect('/dashboard')

@app.route('/parties/<int:id>/delete')
def delete_party(id):
    Party.delete_party({'id':id})
    return redirect('/dashboard')



# def all_parties():
#     all_party=Party.get_all_parties()
#     return render_template("my_parties.html",all_parties=all_party)
@app.route('/my_parties')
def my_parties():
    user_parties = Party.get_user_parties({'user_id':session['user_id']})
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("my_parties.html", parties = user_parties, user = logged_user)

