# Local Imports / Files
from user import create

# Flask App
from flask import Flask
app = Flask(__name__)

#TODO Remove/Update this
# Temporary Exception for failed creation of Users
class NoInput(Exception):
    pass

### PAGE CALLS ###

# Main Page Directory
@app.route("/")
def hewwo():
    return 'Hewwo! ^w^'

# Login Page
@app.route("/login")
def login():
    pass

# User Pages
@app.route("/user/<user_id>")
def show_user(user_id):
    pass

### API CALLS ###

# Create User Function
@app.route("/api/user/create")
def create_user(requests):
    if requests:
        json = requests.get_json()
        if 'name' in json:
            name = json['name']
            if name:
                print("DEBUG: Processing Request")
                return create.addUser()
            else:
                #TODO make status code response instead
                raise NoInput("Name was Empty in Request")
    else:
        #TODO make status code response instead
        raise NoInput("Header was Empty in Request")

### Flask Testing Function ###
def test():
    with app.app_context():
        create.addUser("OwO")

# Invoke of Tester
test()
