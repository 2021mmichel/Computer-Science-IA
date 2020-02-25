import os
from app import app
from flask import Flask, render_template, request, redirect

locations = [

    ]

# app.secret_key = b'h123hfshjdi3'
#
# def index():
#     session['username'] = "Marco"

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:V8DsH51F6HmpDwqP@cluster0-ibvzg.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

# INDEX

@app.route('/')
@app.route('/index')

def index():
    #connect to the Mongo DB
    collection = mongo.db.events
    #find all of the events in that database using a query , store it as events
    #{} will return everything in the database
    #list constructor will turn the results into a list (of dictionaries/objects)
    locations = list(collection.find({}))
    return render_template('index.html', locations = locations)





# CONNECT TO DB, ADD DATA

# @app.route('/signup', methods=['POST', 'GET'])
#
# def signup():
#     if request.method == 'POST':
#         users = mongo.db.users
#         existing_user = users.find_one({'email' : request.form['email']})
#
#         if existing_user is None:
#             users.insert({'email' : request.form['username'], 'password' : request.form['password']})
#             session['email'] = request.form['email']
#             return redirect(url_for('index'))
#
#         return 'That username already exists! Try logging in.'
#
#     return render_template('signup.html')

# need a get and a post method
@app.route('/location_results', methods = ["get", "post"])
def location_results():
    # store userinfo from the form
    user_info = dict(request.form)
    print("the user info is")
    print(user_info)
    #store the general_location
    general_location = user_info["general_location"]
    #store the sport
    sport = user_info["sport"]

    #connect to Mongo DB
    collection = mongo.db.locations
    #insert the user's input event_name and event_date to MONGO
    collection.insert({"general_location": general_location, "sport":sport})
    #(so that it will continue to exist after this program stops)
    #redirect back to the index page

    if general_location == "Harlem" and sport == "Basketball":
        return("Go to Spain!")

    if general_location == "Upper West Side" and sport == "Basketball":
        return("Go to France!")
