# Local Imports / Files
from user import create, interests

# Flask App
from flask import Flask
app = Flask(__name__)

#TODO Remove/Update this
# Temporary Exceptions
class NoInput(Exception):
    pass
class BadInput(Exception):
    pass

### PAGE CALLS ###

#TODO (Maybe - Relies on React-Native front-end)

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

# Create User
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

# Post Interest OR Remove Interest
@app.route("/api/user/interests")
def interests_api(requests):
    if requests:
        json = requests.get_json()
        if 'type' in json:
            type = json['type']
            if type:
                try:
                    arguments = {
                        'user' :json['id'],
                        'interest' :json['interest']
                    }
                    if type == 'add':
                        return interests.add_interest(arguments)
                    elif type == 'remove':
                        return interests.remove_interest(arguments)
                    print("DEBUG: Processing Request")
                except KeyError:
                    #TODO Return Specific invalid arguments status code
                    raise BadInput("Arguments were not given properly")
            else:
                #TODO make status code response instead
                raise NoInput("Name was Empty in Request")
    else:
        #TODO make status code response instead
        raise NoInput("Header was Empty in Request")

### Flask Testing Function ###
def test():
    with app.app_context():
        user = create.addUser("Anubis").get_json()['id']

        # Add Interest Package
        #TODO Add Support for multiple packages being created
        package = {
            'user': user,
            'interest': {
                'name': 'huskies',
                'level': 9999999
            }
        }
        interests.add_interest(package)

        # Add Another Package to Test User
        package = {
            'user': user,
            'interest': {
                'name': 'pokemon',
                'level': 100
            }
        }
        interests.add_interest(package)

        # Add One More Interest
        package = {
            'user': user,
            'interest': {
                'name': 'useless',
                'level': 1
            }
        }
        interests.add_interest(package)

        # Remove Previously added Interest
        interests.remove_interest(package)

# Invoke of Tester
test()
