from flask import render_template, request, redirect

from users_app import app
from users_app.models.User import User



@app.route( "/user", methods=['GET'] )
def displayUsers():
    return render_template( "home.html", users= User.get_all_users())

@app.route( "/user/new", methods=['GET'] )
def displayForm():
    return render_template( "users.html")


@app.route( "/user/new/add", methods=['POST'] )
def addUser():
    print(0)
    first_name =request.form['first_name']
    last_name = request.form['last_name']
    email= request.form['email']
    created_at=['created_at']
    updated_at=['updated_at']
    newUser = User( first_name,last_name,email,created_at,updated_at)
    result = User.add_user(newUser)
    print( result )
    return redirect('/user')



