#Database test

from flask import Flask

from user import create

app = Flask(__name__)

class NoInput(Exception):
    pass

@app.route("/")
def hewwo():
    return 'Hewwo! ^w^'

@app.route("/login")
def login():
    pass

@app.route("/user/<user_id>")
def show_user(user_id):
    pass


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

#Test Function
def test():
    with app.app_context():
        create.addUser("OwO")

test()
