import os
from app import app
from flask import Flask, render_template, request, redirect, session, url_for

locations = [

    ]

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
    #find all of the locations in that database using a query, store it as locations
    #{} will return everything in the database
    #list constructor will turn the results into a list (of dictionaries/objects)
    locations = list(collection.find({}))
    return render_template('index.html', locations = locations)

# signup route
@app.route('/signup', methods=['POST', 'GET'])

def signup():
    # check existing users to ensure a new user ID is being created
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        # if username entered does not match any existing ones, store user ID in MongoDB
        if existing_user is None:
            users.insert({'name' : request.form['username'], 'password' : request.form['password']})
            session['username'] = request.form['username']
            # after successful creation of user ID, redirect user to page of general locations
            return redirect(url_for('general_location'))
        # if the username entered already exists, redirect user to invalid user page
        return redirect(url_for('invalid_user_signup'))

        return 'That username already exists! Try logging in.'

    return render_template('signup.html')

# login route
@app.route('/login', methods = ['POST'])

def login():
    # compare login user to those stored in MongoDB
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    # if username and password are correct, redirect user to page of general locations
    if login_user:
        if request.form['password'] == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('general_location'))
    # if username and password combination is incorrect, redirect user to invalid user page
    return redirect(url_for('invalid_user_login'))

@app.route('/logout')
# when user logs out, clear session
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
    # store locations in MongoDB
    collection = mongo.db.locations
    # create name session
    name = session['username']
    # store locations under user
    locations = collection.find({"user":name})
    return render_template('general_location.html', locations = locations)

# need a get and a post method
@app.route('/general_location_results', methods = ["general_location_list", "POST"])
def general_location_results():
    # store userinfo from the form
    user_info = dict(request.form)
    # store the general_location
    general_location = user_info["general_location"]
    # connect to MongoDB
    collection = mongo.db.general_locations
    # insert the user's input general_location to MongoDB
    collection.insert({"general_location": general_location})
    # (so that it will continue to exist after this program stops)

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

@app.route('/harlem')
def harlem():
    return render_template('harlem.html', locations = locations)

@app.route('/morningside_heights')
def morningside_heights():
    return render_template('morningside_heights.html', locations = locations)

@app.route('/east_harlem')
def east_harlem():
    return render_template('east_harlem.html', locations = locations)

@app.route('/upper_west_side')
def upper_west_side():
    return render_template('upper_west_side.html', locations = locations)

@app.route('/upper_east_side')
def upper_east_side():
    return render_template('upper_east_side.html', locations = locations)

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

# specific location route
@app.route('/specific_location')
def specific_location():
    # store locations in MongoDB
    collection = mongo.db.locations
    # create name session
    name = session['username']
    # store locations under user
    locations = collection.find({"user":name})
    return render_template('specific_location.html', locations = locations)

# get and post method for specific location
@app.route('/specific_location_results', methods = ["specific_location_list", "POST"])
def specific_location_results():
    # store user info from specific location form
    user_info = dict(request.form)
    # store the specific_location
    specific_location = user_info["specific_location"]
    # connect to MongoDB
    collection = mongo.db.specific_locations
    # insert/store user's input specific_location to MongoDB
    collection.insert({"specific_location": specific_location})
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('sport.html', locations = locations, specific_location = specific_location)

@app.route('/alfred_e_smith_recreation_center')
def alfred_e_smith_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('alfred_e_smith_recreation_center.html', locations = locations)

@app.route('/asser_levy_recreation_center')
def asser_levy_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('asser_levy_recreation_center.html', locations = locations)

@app.route('/bryant_park')
def bryant_park():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('bryant_park.html', locations = locations)

@app.route('/central_park')
def central_park():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('central_park.html', locations = locations)

@app.route('/chelsea_piers_basketball')
def chelsea_piers_basketball():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('chelsea_piers_basketball.html', locations = locations)

@app.route('/chelsea_piers_golf')
def chelsea_piers_golf():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('chelsea_piers_golf.html', locations = locations)

@app.route('/chelsea_piers_swim')
def chelsea_piers_swim():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('chelsea_piers_swim.html', locations = locations)

@app.route('/chelsea_recreation_center')
def chelsea_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('chelsea_recreation_center.html', locations = locations)

@app.route('/de_witt_clinton_park')
def de_witt_clinton_park():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('de_witt_clinton_park.html', locations = locations)

@app.route('/equinox_sports_club_new_york')
def equinox_sports_club_new_york():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('equinox_sports_club_new_york.html', locations = locations)

@app.route('/gertrude_ederle_recreation_center')
def gertrude_ederle_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('gertrude_ederle_recreation_center.html', locations = locations)

@app.route('/hamilton_fish_recreation_center')
def hamilton_fish_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('hamilton_fish_recreation_center.html', locations = locations)

@app.route('/hansborough_recreation_center')
def hansborough_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('hansborough_recreation_center.html', locations = locations)

@app.route('/john_v_lindsay_east_river_park')
def john_v_lindsay_east_river_park():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('john_v_lindsay_east_river_park.html', locations = locations)

@app.route('/nyhrc_13th_street')
def nyhrc_13th_street():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('nyhrc_13th_street.html', locations = locations)

@app.route('/nyhrc_21st_street')
def nyhrc_21st_street():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('nyhrc_21st_street.html', locations = locations)

@app.route('/nyhrc_45th_street')
def nyhrc_45th_street():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('nyhrc_45th_street.html', locations = locations)

@app.route('/nyhrc_76th_street')
def nyhrc_76th_street():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('nyhrc_76th_street.html', locations = locations)

@app.route('/nyhrc_whitehall')
def nyhrc_whitehall():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('nyhrc_whitehall.html', locations = locations)

@app.route('/pelham_fritz_recreation_center')
def pelham_fritz_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('pelham_fritz_recreation_center.html', locations = locations)

@app.route('/queensboro_oval')
def queensboro_oval():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('queensboro_oval.html', locations = locations)

@app.route('/recreation_center_54')
def recreation_center_54():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('recreation_center_54.html', locations = locations)

@app.route('/riverside_park_south')
def riverside_park_south():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('riverside_park_south.html', locations = locations)

@app.route('/riverside_park')
def riverside_park():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('riverside_park.html', locations = locations)

@app.route('/sara_d_roosevelt_park')
def sara_d_roosevelt_park():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('sara_d_roosevelt_park.html', locations = locations)

@app.route('/st_catherines_park')
def st_catherines_park():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('st_catherines_park.html', locations = locations)

@app.route('/tanahey_playground')
def tanahey_playground():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('tanahey_playground.html', locations = locations)

@app.route('/thomas_jefferson_park')
def thomas_jefferson_park():
    collection = mongo.db.locations
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('thomas_jefferson_park.html', locations = locations)

@app.route('/thomas_jefferson_recreation_center')
def thomas_jefferson_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('thomas_jefferson_recreation_center.html', locations = locations)

@app.route('/tony_dapolito_recreation_center')
def tony_dapolito_recreation_center():
    collection = mongo.db.locations
    name = session['username']
    locations = list(collection.find({"user":name}))
    return render_template('tony_dapolito_recreation_center.html', locations = locations)

# sport route
@app.route('/sport')
def sport():
    # sports collection
    collection = mongo.db.sports
    name = session['username']
    locations = collection.find({"user":name})
    return render_template('sport.html', locations = locations)

# get and post method for sport
@app.route('/sport_results', methods = ["sport_list", "POST"])
def sport_results():
    user_info = dict(request.form)
    # store user info from sport form
    sport = user_info["sport"]
    # connect to MongoDB (sports collection)
    collection = mongo.db.sports
    # insert/store user's input sport to MongoDB
    collection.insert({"sport": sport})

# Specific location: Harlem and Sport: Basketball

    if user_info["specific_location"] == "125th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "127th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "125th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "127th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "129th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "115th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "117th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "119th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "125th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "127th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "129th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "113th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "115th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "117th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "119th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "121st Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "125th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "127th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "129th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Lenox Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "113th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "115th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "117th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "119th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "121st Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "125th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "127th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "129th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "133rd Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Frederick Douglass Boulevard" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "125th Street and Morningside Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "127th Street and Convent Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "129th Street and Convent Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Convent Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "133rd Street and Convent Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Convent Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "129th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "133rd Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

# Specific location: Morningside Heights and Sport: Basketball

    if user_info["specific_location"] == "111th Street and Manhattan Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "113th Street and Manhattan Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "115th Street and Manhattan Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "117th Street and Manhattan Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "119th Street and Manhattan Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "121st Street and Manhattan Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Manhattan Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "113th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "115th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "117th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "119th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "121st Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "La Salle Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "113th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "115th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "117th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "119th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "121st Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "La Salle Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

# Specific location: East Harlem and Sport: Basketball

    if user_info["specific_location"] == "104th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "108th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "112th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "116th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "120th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "124th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "104th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "108th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "112th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "116th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "120th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "124th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "104th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "108th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "112th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "116th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "120th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "124th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

# Specific location: upper_west_side and Sport: Basketball

    if user_info["specific_location"] == "60th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "65th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "70th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "75th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "80th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "85th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "90th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "95th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "100th Street and West End Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "109th Street and Broadway" and sport == "Basketball":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "60th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "65th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "70th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "75th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "80th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "85th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "90th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "95th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "100th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "109th Street and Amsterdam Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "60th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "65th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "70th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "75th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "80th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "85th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "90th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "95th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "100th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "109th Street and Columbus Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

# Specific location: upper_east_side and Sport: Basketball

    if user_info["specific_location"] == "60th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "75th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "80th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "85th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "90th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "95th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "100th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "60th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "75th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "80th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "85th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "90th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "95th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "100th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "60th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "75th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "80th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "85th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "90th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "95th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "100th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "60th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "75th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "80th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "85th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('equinox_sports_club_new_york'))

    if user_info["specific_location"] == "90th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "95th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

    if user_info["specific_location"] == "100th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('thomas_jefferson_recreation_center'))

# Specific location: midtown_west and Sport: Basketball

    if user_info["specific_location"] == "43rd Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "46th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "49th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "43rd Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "46th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "49th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

# Specific location: midtown_east and Sport: Basketball

    if user_info["specific_location"] == "43rd Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "46th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "49th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "52nd Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "55th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "58th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "43rd Street and Madison Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "46th Street and Madison Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "49th Street and Madison Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "52nd Street and Madison Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "55th Street and Madison Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and Madison Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "43rd Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "46th Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "49th Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "52nd Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "55th Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "58th Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "43rd Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "46th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "49th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "52nd Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "55th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "58th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

# Specific location: times_square and Sport: Basketball

    if user_info["specific_location"] == "43rd Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "45th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "47th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "49th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "43rd Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "45th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "47th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "49th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('gertrude_ederle_recreation_center'))

# Specific location: murray_hill and Sport: Basketball

    if user_info["specific_location"] == "35th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "37th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "39th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "41st Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "35th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "37th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "39th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "41st Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "35th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "37th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "39th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "41st Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "35th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "37th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "39th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "41st Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

# Specific location: garment_district and Sport: Basketball

    if user_info["specific_location"] == "35th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "37th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "39th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "41st Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "35th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "37th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "39th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "41st Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

# Specific location: gramercy and Sport: Basketball

    if user_info["specific_location"] == "16th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "20th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "32nd Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "16th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "20th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "24th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "28th Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "32nd Street and Park Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "16th Street and Irving Place" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "20th Street and Irving Place" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "24th Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "28th Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "32nd Street and Lexington Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "16th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "20th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "24th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "28th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "32nd Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "16th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "20th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "28th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "32nd Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('asser_levy_recreation_center'))

# Specific location: stuyvesant_town and Sport: Basketball

    if user_info["specific_location"] == "15th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "17th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "19th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "21st Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "23rd Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "25th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "27th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "29th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "33rd Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('recreation_center_54'))

# Specific location: chelsea and Sport: Basketball

    if user_info["specific_location"] == "16th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "20th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "32nd Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "16th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "20th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "31st Street and 8th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "16th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_piers_basketball'))

    if user_info["specific_location"] == "20th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "31st Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "36th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "40th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "16th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_piers_basketball'))

    if user_info["specific_location"] == "20th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_piers_basketball'))

    if user_info["specific_location"] == "24th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "31st Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "36th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "40th Street and 10th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_piers_basketball'))

    if user_info["specific_location"] == "28th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "33rd Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "36th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "40th Street and 11th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_recreation_center'))

# Specific location: greenwich_village and Sport: Basketball

    if user_info["specific_location"] == "Leroy Street and Greenwhich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Christopher Street and Greenwhich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Perry Street and Greenwhich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bethune Street and Greenwhich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Horatio Street and Greenwhich Street" and sport == "Basketball":
        return redirect(url_for('chelsea_piers_basketball'))

    if user_info["specific_location"] == "13th Street and 9th Avenue" and sport == "Basketball":
        return redirect(url_for('chelsea_piers_basketball'))

    if user_info["specific_location"] == "Leroy Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Commerce Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Christopher Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Perry Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "13th Street and 7th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bleecker Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "West 4th Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "8th Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "11th Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "13th Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bleecker Street and Thompson Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "3rd Street and Thompson Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "8th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "10th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "12th Street and 5th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bleecker Street and Mercer Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "3rd Street and Mercer Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Washington Place and Mercer Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "8th Street and Mercer Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bond Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "West 4th Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "8th Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

# Specific location: east_village and Sport: Basketball

    if user_info["specific_location"] == "6th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "10th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "14th Street and 3rd Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "2nd Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "6th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "10th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "14th Street and 2nd Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "2nd Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "6th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "10th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "14th Street and 1st Avenue" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue A" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "6th Street and Avenue A" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "10th Street and Avenue A" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "14th Street and Avenue A" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue B" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "6th Street and Avenue B" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "10th Street and Avenue B" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "14th Street and Avenue B" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue C" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "6th Street and Avenue C" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "10th Street and Avenue C" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "14th Street and Avenue C" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue D" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "6th Street and Avenue D" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "10th Street and Avenue D" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "13th Street and Avenue D" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

# Specific location: lower_east_side and Sport: Basketball

    if user_info["specific_location"] == "Pike Street and Cherry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Rutgers Street and Cherry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Clinton Street and Cherry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Montgomery Street and Cherry Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Jackson Street and Cherry Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Pike Street and Madison Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Rutgers Street and Madison Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Clinton Street and Madison Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Montgomery Street and Madison Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Jackson Street and Madison Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Pike Street and Henry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Rutgers Street and Henry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Clinton Street and Henry Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Montgomery Street and Henry Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Jackson Street and Henry Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Pike Street and East Broadway Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Rutgers Street and East Broadway Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Clinton Street and East Broadway Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Montgomery Street and East Broadway Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Norfolk Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Norfolk Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Norfolk Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Norfolk Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Norfolk Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Clinton Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Clinton Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Clinton Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Clinton Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Clinton Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Pitt Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Pitt Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Pitt Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Pitt Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Pitt Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Columbia Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Columbia Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Columbia Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Columbia Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

# Specific location: little_italy and Sport: Basketball

    if user_info["specific_location"] == "Hester Street and Chrystie Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Chrystie Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Chrystie Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Chrystie Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Hester Street and Eldridge Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Eldridge Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Eldridge Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Eldridge Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Hester Street and Orchard Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Orchard Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Orchard Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Orchard Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Hester Street and Essex Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Essex Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Essex Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Essex Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

# Specific location: soho and Sport: Basketball

    if user_info["specific_location"] == "Hester Street and Elizabeth Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Elizabeth Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Elizabeth Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Elizabeth Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Elizabeth Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Hester Street and Mulberry Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Mulberry Street" and sport == "Basketball":
        return redirect(url_for('hamilton_fish_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Mulberry Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Mulberry Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Mulberry Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Howard Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Lafayette Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Howard Street and Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Greene Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Greene Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Greene Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Greene Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and 6th Avenue" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Hudson Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Hudson Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Charlton Street and Hudson Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Charlton Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

# Specific location: tribeca and Sport: Basketball

    if user_info["specific_location"] == "Reade Street and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Thomas Street and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Leonard Street and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "White Street and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Lispenard Street and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Reade Street and Church Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Thomas Street and Church Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Leonard Street and Church Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "White Street and Church Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Lispenard Street and Church Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Reade Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Thomas Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Leonard Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "White Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Lispenard Street and West Broadway" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Reade Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Jay Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Franklin Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Beach Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Laight Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Desbrosses Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('tony_dapolito_recreation_center'))

# Specific location: chinatown and Sport: Basketball

    if user_info["specific_location"] == "Catherine Street and Cherry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Catherine Street and Monroe Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Catherine Street and Henry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Catherine Street and Bowery" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Market Street and Cherry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Market Street and Monroe Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Market Street and Henry Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Market Street and Division Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "St James Place and Madison Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Pearl Street and Park Row" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Centre Street and Worth Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Centre Street and White Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Bayard Street and Baxter Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Bayard Street and Mott Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

# Specific location: financial_district and Sport: Basketball

    if user_info["specific_location"] == "Broad Street and Water Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Old Slip and Water Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Maiden Lane and Water Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Fulton Street and Pearl Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Peck Slip and Pearl Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Broadway and Beaver Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Broad Street and Beaver Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "William Street Beaver Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Wall Street and William Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Cedar Street and William Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Platt Street and William Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Fulton Street and William Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Beekman Street and William Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Battery Place and Broadway" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Rector Street and Broadway" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Liberty Street and Broadway" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Dey Street and Broadway" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Vesey Street and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Park Place and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Warren Street and Broadway" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

    if user_info["specific_location"] == "Battery Place and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Edgar Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Carlisle Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Cedar Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Cortlandt Way and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Vesey Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Park Place and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Warren Street and Greenwich Street" and sport == "Basketball":
        return redirect(url_for('alfred_e_smith_recreation_center'))

# Specific location: Harlem and Sport: Soccer

    if user_info["specific_location"] == "125th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "127th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "125th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "127th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "129th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "131st Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "111th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "115th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "117th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "119th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "125th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "127th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "129th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "131st Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "135th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "111th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "113th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "115th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "117th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "119th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "121st Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "123rd Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "125th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "127th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "129th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "131st Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "135th Street and Lenox Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "111th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "113th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "115th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "117th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "119th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "121st Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "125th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "127th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "129th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "133rd Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "135th Street and Frederick Douglass Boulevard" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "125th Street and Morningside Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "127th Street and Convent Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "129th Street and Convent Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "131st Street and Convent Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "133rd Street and Convent Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "135th Street and Convent Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "129th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "131st Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "133rd Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "135th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

# Specific location: Morningside Heights and Sport: Soccer

    if user_info["specific_location"] == "111th Street and Manhattan Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Manhattan Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "115th Street and Manhattan Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "117th Street and Manhattan Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "119th Street and Manhattan Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "121st Street and Manhattan Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "123rd Street and Manhattan Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "111th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "119th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "121st Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "123rd Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "La Salle Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "111th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "119th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "121st Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "123rd Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "La Salle Street and Broadway" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

# Specific location: East Harlem and Sport: Soccer

    if user_info["specific_location"] == "104th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "108th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "112th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "116th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "120th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "124th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "104th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "108th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "112th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "116th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "120th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "124th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "104th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "108th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "112th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "116th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "120th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "124th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

# Specific location: upper_west_side and Sport: Soccer

    if user_info["specific_location"] == "60th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "65th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "70th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "75th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "80th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "85th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and West End Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Broadway" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "65th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "70th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "75th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "80th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Amsterdam Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "65th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "70th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "75th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('riverside_park_south'))

    if user_info["specific_location"] == "80th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Columbus Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

# Specific location: upper_east_side and Sport: Soccer

    if user_info["specific_location"] == "60th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "65th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "70th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "75th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "80th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "85th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "90th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "100th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "60th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "65th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "70th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "75th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "80th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "85th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "60th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "65th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "70th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "75th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "80th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "85th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('thomas_jefferson_park'))

    if user_info["specific_location"] == "60th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "65th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "70th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "75th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "80th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('central_park'))

# Specific location: midtown_west and Sport: Soccer

    if user_info["specific_location"] == "43rd Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "46th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "49th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "52nd Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "55th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "58th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "43rd Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "46th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "49th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "52nd Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "55th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "58th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "52nd Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "55th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "58th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "52nd Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "55th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "58th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "52nd Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "55th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "58th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

# Specific location: midtown_east and Sport: Soccer

    if user_info["specific_location"] == "43rd Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "46th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "49th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "52nd Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "55th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "58th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "43rd Street and Madison Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "46th Street and Madison Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "49th Street and Madison Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "52nd Street and Madison Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "55th Street and Madison Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "58th Street and Madison Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "43rd Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "46th Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "49th Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "52nd Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "55th Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "58th Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "43rd Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "46th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "49th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "52nd Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "55th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "58th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

# Specific location: times_square and Sport: Soccer

    if user_info["specific_location"] == "43rd Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "45th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "47th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "49th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "43rd Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "45th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "47th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "49th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

# Specific location: murray_hill and Sport: Soccer

    if user_info["specific_location"] == "35th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "37th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "39th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "41st Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "35th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "37th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "39th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "41st Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "35th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "37th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "39th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "41st Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "35th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "37th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "39th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "41st Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

# Specific location: garment_district and Sport: Soccer

    if user_info["specific_location"] == "35th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "37th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "39th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "41st Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "35th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "37th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "39th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "41st Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

# Specific location: gramercy and Sport: Soccer

    if user_info["specific_location"] == "16th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "28th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "16th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "28th Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and Park Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "16th Street and Irving Place" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and Irving Place" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "28th Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "32nd Street and Lexington Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "16th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "28th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "32nd Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

    if user_info["specific_location"] == "16th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "28th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "32nd Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('st_catherines_park'))

# Specific location: stuyvesant_town and Sport: Soccer

    if user_info["specific_location"] == "15th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "17th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "19th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "21st Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "23rd Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "25th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "27th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "29th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "33rd Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: chelsea and Sport: Soccer

    if user_info["specific_location"] == "16th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "28th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "32nd Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "16th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "28th Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "31st Street and 8th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "16th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "24th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "28th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "31st Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "36th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "40th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "16th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "20th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "24th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "28th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "31st Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "36th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "40th Street and 10th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "24th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "28th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "33rd Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "36th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

    if user_info["specific_location"] == "40th Street and 11th Avenue" and sport == "Soccer":
        return redirect(url_for('de_witt_clinton_park'))

# Specific location: greenwich_village and Sport: Soccer

    if user_info["specific_location"] == "Leroy Street and Greenwhich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Christopher Street and Greenwhich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Perry Street and Greenwhich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Bethune Street and Greenwhich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Horatio Street and Greenwhich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "13th Street and 9th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Leroy Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Commerce Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Christopher Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Perry Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "13th Street and 7th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Bleecker Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "West 4th Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "8th Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "11th Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "13th Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Bleecker Street and Thompson Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "3rd Street and Thompson Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "8th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "10th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "12th Street and 5th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Bleecker Street and Mercer Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "3rd Street and Mercer Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Washington Place and Mercer Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "8th Street and Mercer Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Bond Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "West 4th Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "8th Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

# Specific location: east_village and Sport: Soccer

    if user_info["specific_location"] == "6th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "10th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "14th Street and 3rd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "2nd Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "6th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "10th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "14th Street and 2nd Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "2nd Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "6th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "10th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "14th Street and 1st Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "2nd Street and Avenue A" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "6th Street and Avenue A" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "10th Street and Avenue A" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "14th Street and Avenue A" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "2nd Street and Avenue B" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "6th Street and Avenue B" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and Avenue B" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and Avenue B" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and Avenue C" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and Avenue C" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and Avenue C" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and Avenue C" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and Avenue D" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and Avenue D" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and Avenue D" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "13th Street and Avenue D" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: lower_east_side and Sport: Soccer

    if user_info["specific_location"] == "Pike Street and Cherry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Rutgers Street and Cherry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Clinton Street and Cherry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Montgomery Street and Cherry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Jackson Street and Cherry Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Pike Street and Madison Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Rutgers Street and Madison Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Clinton Street and Madison Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Montgomery Street and Madison Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Jackson Street and Madison Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Pike Street and Henry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Rutgers Street and Henry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Clinton Street and Henry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Montgomery Street and Henry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Jackson Street and Henry Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Pike Street and East Broadway Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Rutgers Street and East Broadway Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Clinton Street and East Broadway Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Montgomery Street and East Broadway Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Norfolk Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Norfolk Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Delancey Street and Norfolk Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Rivington Street and Norfolk Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Stanton Street and Norfolk Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Clinton Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Clinton Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Delancey Street and Clinton Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Rivington Street and Clinton Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Stanton Street and Clinton Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Pitt Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Pitt Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Pitt Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rivington Street and Pitt Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Pitt Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Columbia Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Columbia Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Columbia Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rivington Street and Columbia Street" and sport == "Soccer":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: little_italy and Sport: Soccer

    if user_info["specific_location"] == "Hester Street and Chrystie Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Chrystie Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Delancey Street and Chrystie Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Stanton Street and Chrystie Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Hester Street and Eldridge Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Eldridge Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Delancey Street and Eldridge Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Stanton Street and Eldridge Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Hester Street and Orchard Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Orchard Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Delancey Street and Orchard Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Stanton Street and Orchard Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Hester Street and Essex Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Essex Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Delancey Street and Essex Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Stanton Street and Essex Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

# Specific location: soho and Sport: Soccer

    if user_info["specific_location"] == "Hester Street and Elizabeth Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Elizabeth Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Elizabeth Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and Elizabeth Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Prince Street and Elizabeth Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Hester Street and Mulberry Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Mulberry Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Mulberry Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and Mulberry Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Prince Street and Mulberry Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Howard Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Prince Street and Lafayette Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Howard Street and Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Prince Street and Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and Greene Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Greene Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and Greene Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Prince Street and Greene Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Prince Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Grand Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Prince Street and 6th Avenue" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Broome Street and Hudson Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and Hudson Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Charlton Street and Hudson Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Spring Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Charlton Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

# Specific location: tribeca and Sport: Soccer

    if user_info["specific_location"] == "Reade Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Thomas Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Leonard Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "White Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Lispenard Street and Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Reade Street and Church Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Thomas Street and Church Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Leonard Street and Church Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "White Street and Church Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Lispenard Street and Church Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Reade Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Thomas Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Leonard Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "White Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Lispenard Street and West Broadway" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Reade Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Jay Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Franklin Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Beach Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Laight Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

    if user_info["specific_location"] == "Desbrosses Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('sara_d_roosevelt_park'))

# Specific location: chinatown and Sport: Soccer

    if user_info["specific_location"] == "Catherine Street and Cherry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Catherine Street and Monroe Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Catherine Street and Henry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Catherine Street and Bowery" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Market Street and Cherry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Market Street and Monroe Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Market Street and Henry Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Market Street and Division Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "St James Place and Madison Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Pearl Street and Park Row" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Centre Street and Worth Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Centre Street and White Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Bayard Street and Baxter Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Bayard Street and Mott Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

# Specific location: financial_district and Sport: Soccer

    if user_info["specific_location"] == "Broad Street and Water Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Old Slip and Water Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Maiden Lane and Water Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Fulton Street and Pearl Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Peck Slip and Pearl Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Broadway and Beaver Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Broad Street and Beaver Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "William Street Beaver Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Wall Street and William Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Cedar Street and William Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Platt Street and William Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Fulton Street and William Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Beekman Street and William Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Battery Place and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Rector Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Liberty Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Dey Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Vesey Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Park Place and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Warren Street and Broadway" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Battery Place and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Edgar Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Carlisle Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Cedar Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Cortlandt Way and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Vesey Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Park Place and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

    if user_info["specific_location"] == "Warren Street and Greenwich Street" and sport == "Soccer":
        return redirect(url_for('tanahey_playground'))

# Specific location: Harlem and Sport: Tennis

    if user_info["specific_location"] == "125th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "127th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "125th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "127th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "129th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "131st Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "111th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "117th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "119th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "125th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "127th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "129th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "131st Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "135th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "111th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "113th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "115th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "117th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "119th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "121st Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "123rd Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "125th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "127th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "129th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "131st Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "135th Street and Lenox Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "111th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "113th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "115th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "117th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "119th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "121st Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "123rd Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "125th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "127th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "129th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "131st Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "133rd Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "135th Street and Frederick Douglass Boulevard" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "125th Street and Morningside Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "127th Street and Convent Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "129th Street and Convent Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "131st Street and Convent Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "133rd Street and Convent Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "135th Street and Convent Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "129th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "131st Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "133rd Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "135th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

# Specific location: Morningside Heights and Sport: Tennis

    if user_info["specific_location"] == "111th Street and Manhattan Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "113th Street and Manhattan Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "115th Street and Manhattan Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "117th Street and Manhattan Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "119th Street and Manhattan Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "121st Street and Manhattan Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "123rd Street and Manhattan Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "111th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "113th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "115th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "117th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "119th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "121st Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "123rd Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "La Salle Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "111th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "113th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "115th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "117th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "119th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "121st Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "123rd Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "La Salle Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

# Specific location: East Harlem and Sport: Tennis

    if user_info["specific_location"] == "104th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "108th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "112th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "116th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "120th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "124th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "104th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "108th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "112th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "116th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "120th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "124th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "104th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "108th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "112th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "116th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "120th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "124th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

# Specific location: upper_west_side and Sport: Tennis

    if user_info["specific_location"] == "60th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "65th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and West End Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Broadway" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "60th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "65th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Amsterdam Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

    if user_info["specific_location"] == "60th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "65th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Columbus Avenue" and sport == "Tennis":
        return redirect(url_for('riverside_park'))

# Specific location: upper_east_side and Sport: Tennis

    if user_info["specific_location"] == "60th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "65th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "70th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "75th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "80th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "65th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "70th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "75th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "80th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "65th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "70th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "75th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "80th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "65th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "70th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "75th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

# Specific location: midtown_west and Sport: Tennis

    if user_info["specific_location"] == "43rd Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "46th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "58th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "43rd Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "46th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "52nd Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: midtown_east and Sport: Tennis

    if user_info["specific_location"] == "43rd Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "46th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "43rd Street and Madison Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "46th Street and Madison Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and Madison Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and Madison Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and Madison Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and Madison Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "43rd Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "46th Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "43rd Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "46th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "52nd Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "55th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "58th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: times_square and Sport: Tennis

    if user_info["specific_location"] == "43rd Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "45th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "47th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "43rd Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "45th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "47th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "49th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: murray_hill and Sport: Tennis

    if user_info["specific_location"] == "35th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "37th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "39th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "41st Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "35th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "37th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "39th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "41st Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "35th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "37th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "39th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "41st Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "35th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "37th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "39th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "41st Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: garment_district and Sport: Tennis

    if user_info["specific_location"] == "35th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "37th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "39th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "41st Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "35th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "37th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "39th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "41st Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: gramercy and Sport: Tennis

    if user_info["specific_location"] == "16th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "28th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "32nd Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "16th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "28th Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "32nd Street and Park Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "16th Street and Irving Place" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and Irving Place" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "28th Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "32nd Street and Lexington Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "16th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "28th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "32nd Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "16th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "28th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "32nd Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: stuyvesant_town and Sport: Tennis

    if user_info["specific_location"] == "15th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "17th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "19th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "21st Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "23rd Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "25th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "27th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "29th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "33rd Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: chelsea and Sport: Tennis

    if user_info["specific_location"] == "16th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "28th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "32nd Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "16th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "28th Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "31st Street and 8th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "16th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "24th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "28th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "31st Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "36th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "40th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "16th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "20th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "24th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "28th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "31st Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "36th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "40th Street and 10th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "24th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "28th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "33rd Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "36th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

    if user_info["specific_location"] == "40th Street and 11th Avenue" and sport == "Tennis":
        return redirect(url_for('queensboro_oval'))

# Specific location: greenwich_village and Sport: Tennis

    if user_info["specific_location"] == "Leroy Street and Greenwhich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Christopher Street and Greenwhich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Perry Street and Greenwhich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Bethune Street and Greenwhich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Horatio Street and Greenwhich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "13th Street and 9th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Leroy Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Commerce Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Christopher Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Perry Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "13th Street and 7th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Bleecker Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "West 4th Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "8th Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "11th Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "13th Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Bleecker Street and Thompson Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "3rd Street and Thompson Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "8th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "12th Street and 5th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Bleecker Street and Mercer Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "3rd Street and Mercer Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Washington Place and Mercer Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "8th Street and Mercer Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Bond Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "West 4th Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "8th Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: east_village and Sport: Tennis

    if user_info["specific_location"] == "6th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and 3rd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and 2nd Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and 1st Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and Avenue A" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and Avenue A" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and Avenue A" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and Avenue A" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and Avenue B" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and Avenue B" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and Avenue B" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and Avenue B" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and Avenue C" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and Avenue C" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and Avenue C" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "14th Street and Avenue C" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "2nd Street and Avenue D" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "6th Street and Avenue D" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "10th Street and Avenue D" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "13th Street and Avenue D" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: lower_east_side and Sport: Tennis

    if user_info["specific_location"] == "Pike Street and Cherry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rutgers Street and Cherry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Clinton Street and Cherry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Montgomery Street and Cherry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Jackson Street and Cherry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Pike Street and Madison Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rutgers Street and Madison Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Clinton Street and Madison Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Montgomery Street and Madison Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Jackson Street and Madison Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Pike Street and Henry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rutgers Street and Henry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Clinton Street and Henry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Montgomery Street and Henry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Jackson Street and Henry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Pike Street and East Broadway Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rutgers Street and East Broadway Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Clinton Street and East Broadway Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Montgomery Street and East Broadway Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Norfolk Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Norfolk Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Norfolk Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rivington Street and Norfolk Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Norfolk Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Clinton Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Clinton Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Clinton Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rivington Street and Clinton Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Clinton Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Pitt Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Pitt Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Pitt Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rivington Street and Pitt Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Pitt Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Columbia Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Columbia Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Columbia Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rivington Street and Columbia Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: little_italy and Sport: Tennis

    if user_info["specific_location"] == "Hester Street and Chrystie Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Chrystie Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Chrystie Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Chrystie Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Hester Street and Eldridge Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Eldridge Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Eldridge Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Eldridge Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Hester Street and Orchard Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Orchard Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Orchard Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Orchard Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Hester Street and Essex Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Essex Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Delancey Street and Essex Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Stanton Street and Essex Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: soho and Sport: Tennis

    if user_info["specific_location"] == "Hester Street and Elizabeth Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Elizabeth Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Elizabeth Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and Elizabeth Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Prince Street and Elizabeth Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Hester Street and Mulberry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Mulberry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Mulberry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and Mulberry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Prince Street and Mulberry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Howard Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Prince Street and Lafayette Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Howard Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Prince Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and Greene Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Greene Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and Greene Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Prince Street and Greene Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Prince Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Grand Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Prince Street and 6th Avenue" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broome Street and Hudson Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and Hudson Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Charlton Street and Hudson Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Spring Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Charlton Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: tribeca and Sport: Tennis

    if user_info["specific_location"] == "Reade Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Thomas Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Leonard Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "White Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Lispenard Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Reade Street and Church Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Thomas Street and Church Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Leonard Street and Church Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "White Street and Church Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Lispenard Street and Church Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Reade Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Thomas Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Leonard Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "White Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Lispenard Street and West Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Reade Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Jay Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Franklin Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Beach Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Laight Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Desbrosses Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: chinatown and Sport: Tennis

    if user_info["specific_location"] == "Catherine Street and Cherry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Catherine Street and Monroe Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Catherine Street and Henry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Catherine Street and Bowery" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Market Street and Cherry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Market Street and Monroe Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Market Street and Henry Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Market Street and Division Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "St James Place and Madison Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Pearl Street and Park Row" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Centre Street and Worth Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Centre Street and White Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Bayard Street and Baxter Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Bayard Street and Mott Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: financial_district and Sport: Tennis

    if user_info["specific_location"] == "Broad Street and Water Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Old Slip and Water Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Maiden Lane and Water Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Fulton Street and Pearl Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Peck Slip and Pearl Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broadway and Beaver Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Broad Street and Beaver Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "William Street Beaver Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Wall Street and William Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Cedar Street and William Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Platt Street and William Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Fulton Street and William Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Beekman Street and William Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Battery Place and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Rector Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Liberty Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Dey Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Vesey Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Park Place and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Warren Street and Broadway" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Battery Place and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Edgar Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Carlisle Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Cedar Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Cortlandt Way and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Vesey Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Park Place and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

    if user_info["specific_location"] == "Warren Street and Greenwich Street" and sport == "Tennis":
        return redirect(url_for('john_v_lindsay_east_river_park'))

# Specific location: anything and Sport: Golf

    if sport == "Golf":
        return redirect(url_for('chelsea_piers_golf'))

# Specific location: Harlem and Sport: Ice Skate

    if user_info["specific_location"] == "125th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "127th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "125th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "127th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "129th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "131st Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "111th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "119th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "125th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "127th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "129th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "131st Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "135th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "111th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "119th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "121st Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "123rd Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "125th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "127th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "129th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "131st Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "135th Street and Lenox Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "111th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "119th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "121st Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "123rd Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "125th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "127th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "129th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "131st Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "133rd Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "135th Street and Frederick Douglass Boulevard" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "125th Street and Morningside Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "127th Street and Convent Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "129th Street and Convent Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "131st Street and Convent Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "133rd Street and Convent Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "135th Street and Convent Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "129th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "131st Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "133rd Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "135th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

# Specific location: Morningside Heights and Sport: Ice Skate

    if user_info["specific_location"] == "111th Street and Manhattan Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Manhattan Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and Manhattan Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and Manhattan Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "119th Street and Manhattan Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "121st Street and Manhattan Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "123rd Street and Manhattan Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "111th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "119th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "121st Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "123rd Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "La Salle Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "111th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "113th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "115th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "117th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "119th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "121st Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "123rd Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "La Salle Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

# Specific location: East Harlem and Sport: Ice Skate

    if user_info["specific_location"] == "104th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "108th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "112th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "116th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "120th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "124th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "104th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "108th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "112th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "116th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "120th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "124th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "104th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "108th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "112th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "116th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "120th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "124th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

# Specific location: upper_west_side and Sport: Ice Skate

    if user_info["specific_location"] == "60th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "65th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and West End Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "65th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Amsterdam Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "65th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "109th Street and Columbus Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

# Specific location: upper_east_side and Sport: Ice Skate

    if user_info["specific_location"] == "60th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "65th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "70th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "65th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "65th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "70th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "60th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "65th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "70th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "75th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "80th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "85th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "90th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "95th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "100th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

# Specific location: midtown_west and Sport: Ice Skate

    if user_info["specific_location"] == "43rd Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "46th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('central_park'))

    if user_info["specific_location"] == "43rd Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "46th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: midtown_east and Sport: Ice Skate

    if user_info["specific_location"] == "43rd Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "46th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "43rd Street and Madison Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "46th Street and Madison Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and Madison Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and Madison Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and Madison Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and Madison Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "43rd Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "46th Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "43rd Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "46th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "52nd Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "55th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "58th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: times_square and Sport: Ice Skate

    if user_info["specific_location"] == "43rd Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "45th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "47th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "43rd Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "45th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "47th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "49th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: murray_hill and Sport: Ice Skate

    if user_info["specific_location"] == "35th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "37th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "39th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "41st Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "35th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "37th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "39th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "41st Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "35th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "37th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "39th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "41st Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "35th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "37th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "39th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "41st Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: garment_district and Sport: Ice Skate

    if user_info["specific_location"] == "35th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "37th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "39th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "41st Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "35th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "37th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "39th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "41st Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: gramercy and Sport: Ice Skate

    if user_info["specific_location"] == "16th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "16th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and Park Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "16th Street and Irving Place" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and Irving Place" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and Lexington Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "16th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "16th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: stuyvesant_town and Sport: Ice Skate

    if user_info["specific_location"] == "15th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "17th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "19th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "21st Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "23rd Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "25th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "27th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "29th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "33rd Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: chelsea and Sport: Ice Skate

    if user_info["specific_location"] == "16th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "32nd Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "16th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "31st Street and 8th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "16th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "31st Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "36th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "40th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "16th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "20th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "31st Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "36th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "40th Street and 10th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "24th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "28th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "33rd Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "36th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "40th Street and 11th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: greenwich_village and Sport: Ice Skate

    if user_info["specific_location"] == "Leroy Street and Greenwhich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Christopher Street and Greenwhich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Perry Street and Greenwhich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Bethune Street and Greenwhich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Horatio Street and Greenwhich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "13th Street and 9th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Leroy Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Commerce Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Christopher Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Perry Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "13th Street and 7th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Bleecker Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "West 4th Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "8th Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "11th Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "13th Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Bleecker Street and Thompson Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "3rd Street and Thompson Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "8th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "12th Street and 5th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Bleecker Street and Mercer Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "3rd Street and Mercer Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Washington Place and Mercer Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "8th Street and Mercer Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Bond Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "West 4th Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "8th Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: east_village and Sport: Ice Skate

    if user_info["specific_location"] == "6th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "14th Street and 3rd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "2nd Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "6th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "14th Street and 2nd Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "2nd Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "6th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "14th Street and 1st Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "2nd Street and Avenue A" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "6th Street and Avenue A" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and Avenue A" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "14th Street and Avenue A" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "2nd Street and Avenue B" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "6th Street and Avenue B" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and Avenue B" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "14th Street and Avenue B" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "2nd Street and Avenue C" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "6th Street and Avenue C" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and Avenue C" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "14th Street and Avenue C" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "2nd Street and Avenue D" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "6th Street and Avenue D" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "10th Street and Avenue D" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "13th Street and Avenue D" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: lower_east_side and Sport: Ice Skate

    if user_info["specific_location"] == "Pike Street and Cherry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rutgers Street and Cherry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Clinton Street and Cherry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Montgomery Street and Cherry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Jackson Street and Cherry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Pike Street and Madison Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rutgers Street and Madison Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Clinton Street and Madison Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Montgomery Street and Madison Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Jackson Street and Madison Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Pike Street and Henry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rutgers Street and Henry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Clinton Street and Henry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Montgomery Street and Henry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Jackson Street and Henry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Pike Street and East Broadway Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rutgers Street and East Broadway Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Clinton Street and East Broadway Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Montgomery Street and East Broadway Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Norfolk Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Norfolk Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Norfolk Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rivington Street and Norfolk Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Stanton Street and Norfolk Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Clinton Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Clinton Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Clinton Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rivington Street and Clinton Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Stanton Street and Clinton Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Pitt Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Pitt Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Pitt Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rivington Street and Pitt Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Stanton Street and Pitt Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Columbia Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Columbia Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Columbia Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rivington Street and Columbia Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: little_italy and Sport: Ice Skate

    if user_info["specific_location"] == "Hester Street and Chrystie Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Chrystie Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Chrystie Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Stanton Street and Chrystie Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Hester Street and Eldridge Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Eldridge Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Eldridge Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Stanton Street and Eldridge Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Hester Street and Orchard Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Orchard Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Orchard Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Stanton Street and Orchard Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Hester Street and Essex Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Essex Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Delancey Street and Essex Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Stanton Street and Essex Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: soho and Sport: Ice Skate

    if user_info["specific_location"] == "Hester Street and Elizabeth Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Elizabeth Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Elizabeth Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and Elizabeth Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Prince Street and Elizabeth Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Hester Street and Mulberry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Mulberry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Mulberry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and Mulberry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Prince Street and Mulberry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Howard Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Prince Street and Lafayette Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Howard Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Prince Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and Greene Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Greene Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and Greene Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Prince Street and Greene Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Prince Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Grand Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Prince Street and 6th Avenue" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broome Street and Hudson Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and Hudson Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Charlton Street and Hudson Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Spring Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Charlton Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: tribeca and Sport: Ice Skate

    if user_info["specific_location"] == "Reade Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Thomas Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Leonard Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "White Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Lispenard Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Reade Street and Church Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Thomas Street and Church Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Leonard Street and Church Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "White Street and Church Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Lispenard Street and Church Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Reade Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Thomas Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Leonard Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "White Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Lispenard Street and West Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Reade Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Jay Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Franklin Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Beach Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Laight Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Desbrosses Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: chinatown and Sport: Ice Skate

    if user_info["specific_location"] == "Catherine Street and Cherry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Catherine Street and Monroe Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Catherine Street and Henry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Catherine Street and Bowery" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Market Street and Cherry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Market Street and Monroe Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Market Street and Henry Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Market Street and Division Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "St James Place and Madison Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Pearl Street and Park Row" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Centre Street and Worth Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Centre Street and White Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Bayard Street and Baxter Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Bayard Street and Mott Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: financial_district and Sport: Ice Skate

    if user_info["specific_location"] == "Broad Street and Water Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Old Slip and Water Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Maiden Lane and Water Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Fulton Street and Pearl Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Peck Slip and Pearl Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broadway and Beaver Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Broad Street and Beaver Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "William Street Beaver Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Wall Street and William Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Cedar Street and William Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Platt Street and William Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Fulton Street and William Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Beekman Street and William Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Battery Place and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Rector Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Liberty Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Dey Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Vesey Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Park Place and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Warren Street and Broadway" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Battery Place and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Edgar Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Carlisle Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Cedar Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Cortlandt Way and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Vesey Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Park Place and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

    if user_info["specific_location"] == "Warren Street and Greenwich Street" and sport == "Ice Skate":
        return redirect(url_for('bryant_park'))

# Specific location: Harlem and Sport: Swim

    if user_info["specific_location"] == "125th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "127th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "125th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "127th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "129th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "115th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "117th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "119th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "125th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "127th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "129th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "113th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "115th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "117th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "119th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "121st Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "125th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "127th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "129th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Lenox Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "111th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "113th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "115th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "117th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "119th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "121st Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "125th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "127th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "129th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "133rd Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Frederick Douglass Boulevard" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "125th Street and Morningside Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "127th Street and Convent Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "129th Street and Convent Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Convent Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "133rd Street and Convent Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Convent Avenue" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "129th Street and Broadway" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "131st Street and Broadway" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "133rd Street and Broadway" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

    if user_info["specific_location"] == "135th Street and Broadway" and sport == "Swim":
        return redirect(url_for('hansborough_recreation_center'))

# Specific location: Morningside Heights and Sport: Swim

    if user_info["specific_location"] == "111th Street and Manhattan Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "113th Street and Manhattan Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "115th Street and Manhattan Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "117th Street and Manhattan Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "119th Street and Manhattan Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "121st Street and Manhattan Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Manhattan Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "111th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "113th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "115th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "117th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "119th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "121st Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "La Salle Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "111th Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "113th Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "115th Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "117th Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "119th Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "121st Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "123rd Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "La Salle Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

# Specific location: East Harlem and Sport: Swim

    if user_info["specific_location"] == "104th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "108th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "112th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "116th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "120th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "124th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "104th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "108th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "112th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "116th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "120th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "124th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "104th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "108th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "112th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "116th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "120th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "124th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

# Specific location: upper_west_side and Sport: Swim

    if user_info["specific_location"] == "60th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "65th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "70th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "75th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "80th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "85th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "90th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "95th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "100th Street and West End Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "109th Street and Broadway" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "60th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "65th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "70th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "75th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "80th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "85th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "90th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "95th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "100th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "109th Street and Amsterdam Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "60th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "65th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "70th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "75th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "80th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "85th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "90th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "95th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "100th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

    if user_info["specific_location"] == "109th Street and Columbus Avenue" and sport == "Swim":
        return redirect(url_for('pelham_fritz_recreation_center'))

# Specific location: upper_east_side and Sport: Swim

    if user_info["specific_location"] == "60th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "75th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "80th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "85th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "90th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "95th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "100th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "60th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "75th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "80th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "85th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "90th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "95th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "100th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "60th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "75th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "80th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "85th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "90th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "95th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "100th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "60th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "65th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "70th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "75th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "80th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "85th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "90th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "95th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

    if user_info["specific_location"] == "100th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_76th_street'))

# Specific location: midtown_west and Sport: Swim

    if user_info["specific_location"] == "43rd Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "46th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "49th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "43rd Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "46th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "49th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "52nd Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "55th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "58th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

# Specific location: midtown_east and Sport: Swim

    if user_info["specific_location"] == "43rd Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "46th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "49th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "52nd Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "55th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "58th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "43rd Street and Madison Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "46th Street and Madison Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "49th Street and Madison Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "52nd Street and Madison Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "55th Street and Madison Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "58th Street and Madison Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "43rd Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "46th Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "49th Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "52nd Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "55th Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "58th Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "43rd Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "46th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "49th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "52nd Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "55th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

    if user_info["specific_location"] == "58th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('recreation_center_54'))

# Specific location: times_square and Sport: Swim

    if user_info["specific_location"] == "43rd Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "45th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "47th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "49th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "43rd Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "45th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "47th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

    if user_info["specific_location"] == "49th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('gertrude_ederle_recreation_center'))

# Specific location: murray_hill and Sport: Swim

    if user_info["specific_location"] == "35th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "37th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "39th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "41st Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "35th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "37th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "39th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "41st Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "35th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "37th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "39th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "41st Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "35th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "37th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "39th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "41st Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

# Specific location: garment_district and Sport: Swim

    if user_info["specific_location"] == "35th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "37th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "39th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "41st Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_45th_street'))

    if user_info["specific_location"] == "35th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "37th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "39th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "41st Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

# Specific location: gramercy and Sport: Swim

    if user_info["specific_location"] == "16th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "20th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "24th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "28th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "32nd Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "16th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "20th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "24th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "28th Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "32nd Street and Park Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "16th Street and Irving Place" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "20th Street and Irving Place" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "24th Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "28th Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "32nd Street and Lexington Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "16th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "20th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "24th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "28th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "32nd Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "16th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "20th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_21st_street'))

    if user_info["specific_location"] == "24th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "28th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "32nd Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

# Specific location: stuyvesant_town and Sport: Swim

    if user_info["specific_location"] == "15th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "17th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "19th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "21st Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "23rd Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "25th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "27th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "29th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "33rd Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

# Specific location: chelsea and Sport: Swim

    if user_info["specific_location"] == "16th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "20th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "32nd Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "16th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "20th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "31st Street and 8th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "16th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_piers_swim'))

    if user_info["specific_location"] == "20th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "31st Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "36th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "40th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "16th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_piers_swim'))

    if user_info["specific_location"] == "20th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_piers_swim'))

    if user_info["specific_location"] == "24th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "28th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "31st Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "36th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "40th Street and 10th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "24th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_piers_swim'))

    if user_info["specific_location"] == "28th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "33rd Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "36th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

    if user_info["specific_location"] == "40th Street and 11th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_recreation_center'))

# Specific location: greenwich_village and Sport: Swim

    if user_info["specific_location"] == "Leroy Street and Greenwhich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Christopher Street and Greenwhich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Perry Street and Greenwhich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bethune Street and Greenwhich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Horatio Street and Greenwhich Street" and sport == "Swim":
        return redirect(url_for('chelsea_piers_swim'))

    if user_info["specific_location"] == "13th Street and 9th Avenue" and sport == "Swim":
        return redirect(url_for('chelsea_piers_swim'))

    if user_info["specific_location"] == "Leroy Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Commerce Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Christopher Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Perry Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "13th Street and 7th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Bleecker Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "West 4th Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "8th Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "11th Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "13th Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Bleecker Street and Thompson Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "3rd Street and Thompson Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "8th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "10th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "12th Street and 5th Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Bleecker Street and Mercer Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "3rd Street and Mercer Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Washington Place and Mercer Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "8th Street and Mercer Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Bond Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "West 4th Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "8th Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

# Specific location: east_village and Sport: Swim

    if user_info["specific_location"] == "6th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "10th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "14th Street and 3rd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "2nd Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "6th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "10th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "14th Street and 2nd Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "2nd Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "6th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "10th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "14th Street and 1st Avenue" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue A" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "6th Street and Avenue A" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "10th Street and Avenue A" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "14th Street and Avenue A" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue B" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "6th Street and Avenue B" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "10th Street and Avenue B" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "14th Street and Avenue B" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue C" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "6th Street and Avenue C" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "10th Street and Avenue C" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "14th Street and Avenue C" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "2nd Street and Avenue D" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "6th Street and Avenue D" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "10th Street and Avenue D" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

    if user_info["specific_location"] == "13th Street and Avenue D" and sport == "Swim":
        return redirect(url_for('asser_levy_recreation_center'))

# Specific location: lower_east_side and Sport: Swim

    if user_info["specific_location"] == "Pike Street and Cherry Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Rutgers Street and Cherry Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Clinton Street and Cherry Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Montgomery Street and Cherry Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Jackson Street and Cherry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Pike Street and Madison Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Rutgers Street and Madison Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Clinton Street and Madison Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Montgomery Street and Madison Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Jackson Street and Madison Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Pike Street and Henry Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Rutgers Street and Henry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Clinton Street and Henry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Montgomery Street and Henry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Jackson Street and Henry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Pike Street and East Broadway Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Rutgers Street and East Broadway Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Clinton Street and East Broadway Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Montgomery Street and East Broadway Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Norfolk Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Norfolk Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Norfolk Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Norfolk Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Norfolk Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Clinton Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Clinton Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Clinton Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Clinton Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Clinton Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Pitt Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Pitt Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Pitt Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Pitt Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Pitt Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Columbia Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Columbia Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Columbia Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Rivington Street and Columbia Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

# Specific location: little_italy and Sport: Swim

    if user_info["specific_location"] == "Hester Street and Chrystie Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Chrystie Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Chrystie Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Chrystie Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Hester Street and Eldridge Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Eldridge Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Eldridge Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Stanton Street and Eldridge Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Hester Street and Orchard Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Orchard Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Orchard Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Stanton Street and Orchard Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Hester Street and Essex Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Essex Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Delancey Street and Essex Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

    if user_info["specific_location"] == "Stanton Street and Essex Street" and sport == "Swim":
        return redirect(url_for('nyhrc_13th_street'))

# Specific location: soho and Sport: Swim

    if user_info["specific_location"] == "Hester Street and Elizabeth Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Elizabeth Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Elizabeth Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Elizabeth Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Elizabeth Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Hester Street and Mulberry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Mulberry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Mulberry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Mulberry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Mulberry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Howard Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Lafayette Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Howard Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and Greene Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Greene Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Greene Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and Greene Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Grand Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Prince Street and 6th Avenue" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Broome Street and Hudson Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Hudson Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Charlton Street and Hudson Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Spring Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Charlton Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

# Specific location: tribeca and Sport: Swim

    if user_info["specific_location"] == "Reade Street and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Thomas Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Leonard Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "White Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Lispenard Street and Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Reade Street and Church Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Thomas Street and Church Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Leonard Street and Church Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "White Street and Church Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Lispenard Street and Church Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Reade Street and West Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Thomas Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Leonard Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "White Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Lispenard Street and West Broadway" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Reade Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Jay Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Franklin Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Beach Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Laight Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Desbrosses Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

# Specific location: chinatown and Sport: Swim

    if user_info["specific_location"] == "Catherine Street and Cherry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Catherine Street and Monroe Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Catherine Street and Henry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Catherine Street and Bowery" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Market Street and Cherry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Market Street and Monroe Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Market Street and Henry Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Market Street and Division Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "St James Place and Madison Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Pearl Street and Park Row" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Centre Street and Worth Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Centre Street and White Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bayard Street and Baxter Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

    if user_info["specific_location"] == "Bayard Street and Mott Street" and sport == "Swim":
        return redirect(url_for('tony_dapolito_recreation_center'))

# Specific location: financial_district and Sport: Swim

    if user_info["specific_location"] == "Broad Street and Water Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Old Slip and Water Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Maiden Lane and Water Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Fulton Street and Pearl Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Peck Slip and Pearl Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Broadway and Beaver Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Broad Street and Beaver Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "William Street Beaver Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Wall Street and William Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Cedar Street and William Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Platt Street and William Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Fulton Street and William Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Beekman Street and William Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Battery Place and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Rector Street and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Liberty Street and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Dey Street and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Vesey Street and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Park Place and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Warren Street and Broadway" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Battery Place and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Edgar Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Carlisle Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Cedar Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Cortlandt Way and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Vesey Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Park Place and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))

    if user_info["specific_location"] == "Warren Street and Greenwich Street" and sport == "Swim":
        return redirect(url_for('nyhrc_whitehall'))
