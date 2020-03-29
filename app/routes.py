import os
from app import app
from flask import Flask, render_template, request, redirect, session, url_for

locations = [

    ]


#
# def index():
#     session['username'] = "Marco"

from flask_pymongo import PyMongo

app.secret_key = b'h123hfshjdi3/'

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
    collection = mongo.db.locations
    #find all of the events in that database using a query , store it as events
    #{} will return everything in the database
    #list constructor will turn the results into a list (of dictionaries/objects)
    locations = list(collection.find({}))
    return render_template('index.html', locations = locations)


# CONNECT TO DB, ADD DATA

@app.route('/signup', methods=['POST', 'GET'])

def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            users.insert({'name' : request.form['username'], 'password' : request.form['password']})
            session['username'] = request.form['username']
            return redirect(url_for('general_location'))

        return redirect(url_for('invalid_user_signup'))

        return 'That username already exists! Try logging in.'

    return render_template('signup.html')

@app.route('/login', methods = ['POST'])

def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if request.form['password'] == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('general_location'))

    return redirect(url_for('invalid_user_login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/index')

@app.route('/mylocations')
def mylocations():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('person.html', locations = locations)

@app.route('/invalid_user_login')
def invalid_user_login():
    return render_template('invalid_user_login.html', locations = locations)

@app.route('/invalid_user_signup')
def invalid_user_signup():
    return render_template('invalid_user_signup.html', locations = locations)

@app.route('/general_location')
def general_location():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('general_location.html', locations = locations)

# need a get and a post method
@app.route('/general_location_results', methods = ["general_location_list", "POST"])
def general_location_results():
    # store userinfo from the form
    user_info = dict(request.form)
    # print("the user info is")
    # print(user_info)
    #store the general_location
    general_location = user_info["general_location"]
    # #store the sport
    # sport = user_info["sport"]
    #connect to Mongo DB
    collection = mongo.db.locations
    #insert the user's input event_name and event_date to MONGO
    collection.insert({"general_location": general_location})
    #(so that it will continue to exist after this program stops)
    #redirect back to the index page

    if general_location == "Harlem":
        return redirect(url_for('harlem'))

    if general_location == "Morningside Heights":
        return redirect(url_for('morningside_heights'))

    if general_location == "East Harlem":
        return redirect(url_for('east_harlem'))

    if general_location == "Upper West Side":
        return redirect(url_for('upper_west_side'))

    if general_location == "Upper East Side":
        return redirect(url_for('upper_east_side'))

    if general_location == "Midtown West":
        return redirect(url_for('midtown_west'))

    if general_location == "Midtown East":
        return redirect(url_for('midtown_east'))

    if general_location == "Times Square":
        return redirect(url_for('times_square'))

    if general_location == "Murray Hill":
        return redirect(url_for('murray_hill'))

    if general_location == "Garment District":
        return redirect(url_for('garment_district'))

    if general_location == "Gramercy":
        return redirect(url_for('gramercy'))

    if general_location == "Stuyvesant Town":
        return redirect(url_for('stuyvesant_town'))

    if general_location == "Chelsea":
        return redirect(url_for('chelsea'))

    if general_location == "Greenwich Village":
        return redirect(url_for('greenwich_village'))

    if general_location == "East Village":
        return redirect(url_for('east_village'))

    if general_location == "Lower East Side":
        return redirect(url_for('lower_east_side'))

    if general_location == "Little Italy":
        return redirect(url_for('little_italy'))

    if general_location == "Soho":
        return redirect(url_for('soho'))

    if general_location == "Tribeca":
        return redirect(url_for('tribeca'))

    if general_location == "Chinatown":
        return redirect(url_for('chinatown'))

    if general_location == "Financial District":
        return redirect(url_for('financial_district'))

    # if general_location == "Upper West Side" and sport == "Basketball":
    #     return("Go to France!")

@app.route('/harlem')
def harlem():
    return render_template('harlem.html', locations = locations)

@app.route('/morningside_heights')
def morningside_heights():
    return render_template('morningside_heights.html', locations = locations)

@app.route('/east_harlem')
def east_harlem():
    return render_template('east_harlem.html', locations = locations)

@app.route('/midtown_west')
def midtown_west():
    return render_template('midtown_west.html', locations = locations)

@app.route('/midtown_east')
def midtown_east():
    return render_template('midtown_east.html', locations = locations)

@app.route('/times_square')
def times_square():
    return render_template('times_square.html', locations = locations)

@app.route('/murray_hill')
def murray_hill():
    return render_template('murray_hill.html', locations = locations)

@app.route('/garment_district')
def garment_district():
    return render_template('garment_district.html', locations = locations)

@app.route('/gramercy')
def gramercy():
    return render_template('gramercy.html', locations = locations)

@app.route('/stuyvesant_town')
def stuyvesant_town():
    return render_template('stuyvesant_town.html', locations = locations)

@app.route('/chelsea')
def chelsea():
    return render_template('chelsea.html', locations = locations)

@app.route('/greenwich_village')
def greenwich_village():
    return render_template('greenwich_village.html', locations = locations)

@app.route('/east_village')
def east_village():
    return render_template('east_village.html', locations = locations)

@app.route('/lower_east_side')
def lower_east_side():
    return render_template('lower_east_side.html', locations = locations)

@app.route('/little_italy')
def little_italy():
    return render_template('little_italy.html', locations = locations)

@app.route('/soho')
def soho():
    return render_template('soho.html', locations = locations)

@app.route('/tribeca')
def tribeca():
    return render_template('tribeca.html', locations = locations)

@app.route('/chinatown')
def chinatown():
    return render_template('chinatown.html', locations = locations)

@app.route('/financial_district')
def financial_district():
    return render_template('financial_district.html', locations = locations)

@app.route('/sport')
def sport():
    return render_template('sport.html', locations = locations)

@app.route('/specific_location')
def specific_location():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('specific_location.html', locations = locations)

@app.route('/specific_location_results', methods = ["specific_location_list", "POST"])
def specific_location_results():
    user_info = dict(request.form)
    specific_location = user_info["specific_location"]
    collection = mongo.db.locations
    collection.insert({"specific_location": specific_location})
    #(so that it will continue to exist after this program stops)
    #redirect back to the index page

# @app.route('/general_location')
# def general_location():
