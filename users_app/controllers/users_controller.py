from types import new_class
from flask import render_template, request, redirect
from flask.globals import session

from users_app import app

from users_app.models.User import User



@app.route( "/user", methods=['GET'] )
def displayUsers():
    return render_template( "home.html", users=User.get_all_users())

@app.route( "/user/new", methods=['GET'] )
def displayForm():
    return render_template( "users.html")


@app.route( "/user/new/add", methods=['POST'] )
def addUser():
    print(0)
    id=['id']
    first_name =request.form['first_name']
    last_name = request.form['last_name']
    email= request.form['email']
    created_at=['created_at']
    updated_at=['updated_at']
    newUser = User(id,first_name, last_name, email, created_at, updated_at)
    result = User.add_user(newUser)
    print( result )
    return redirect('/user')


@app.route('/user/edit/<id>')
def edit(id):
    data ={ 
        "id":int(id)
    }
    newUser=User(data)
    result=User.get_one(newUser)
    return render_template("edit.html")

@app.route('/user/show/<id>',methods=['GET'])
def show(id):
    data ={ 
        "id":int(id),
       
        
    }
    
    return render_template("show.html",user=User.get_one_user(data))


@app.route('/user/update',methods=['POST'])
def update():
    id=['id']
    first_name =request.form['first_name']
    last_name = request.form['last_name']
    email= request.form['email']
    created_at=['created_at']
    updated_at=['updated_at']
    newUser = User( id,first_name,last_name,email,created_at,updated_at)
    result = User.update(newUser)
    return result,redirect('/user')

@app.route('/user/delete/<id>')
def delete(id):
    data ={
        "id": int(id)
    }
    User.delete(data)
    return redirect('/user')


