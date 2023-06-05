from flask_app import app
from flask_app.models.user import User
from flask_app.models.show import Show
from flask import request , redirect, session, render_template, flash


@app.route('/shows')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_shows = Show.get_all_shows()
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html",user=logged_user, shows=all_shows)


@app.route('/shows/new' )
def new_show():
    if 'user_id' not in session:
        return redirect('/') 
    return render_template("new_show.html") 

@app.route('/shows/add', methods=['POST'])
def add_show():
    if 'user_id' not in session:
        return redirect('/') 
    if not Show.validate_show(request.form):
        return redirect("/shows/new")
    data = {
        **request.form,
        'user_id': session["user_id"] 
    }
    Show.create_show(data)
    
    return redirect("/shows")

@app.route('/shows/edit/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/') 
    show = Show.get_by_id({'id':id})
    return render_template("edit_show.html",  show = show)


@app.route('/shows/update/<int:id>',methods=['post'])
def update_show(id):
    if not Show.validate_show(request.form):
        return redirect(f"/shows/edit/{id}")
    Show.update_show(request.form)
    return redirect('/shows')

@app.route('/shows/<int:id>/delete')
def delete_show(id):
    Show.delete_show({'id':id})
    return redirect('/shows')

@app.route('/shows/<int:id>')
def show_one(id):
    if 'user_id' not in session:
        return redirect('/') 
    show = Show.get_by_id({'id':id})
    return render_template("view_show.html", show = show)