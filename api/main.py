# Local Imports / Files
from user import create, interests

# Flask App
from flask import Flask

import asyncio

app = Flask(__name__)

# TODO Remove/Update this
# Temporary Exceptions


class NoInput(Exception):
    pass


class BadInput(Exception):
    pass

### PAGE CALLS ###

# TODO (Maybe - Relies on React-Native front-end)

# Main Page Directory


@app.route("/")
def main_page():
    return 'Hewwo! ^w^'

# Login Page


@app.route("/login")
def login_page():
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
                return create.addUser()
            else:
                # TODO make status code response instead
                raise NoInput("Name was Empty in Request")
    else:
        # TODO make status code response instead
        raise NoInput("Header was Empty in Request")

# All Interest Actions

@app.route("/api/user/interests")
def interests_api(requests):
    if requests:
        json = requests.get_json()
        if 'type' in json and json['type']:
            type = json['type']
            try:
                arguments = {
                    'user': json['id'],
                    'interest': json['interest']
                }
                if type == 'add':
                    return interests.add_interest(arguments)
                elif type == 'remove':
                    return interests.remove_interest(arguments)
                elif type == 'get':
                    return interests.get_interest(arguments)
            except KeyError:
                # TODO Return Specific invalid arguments status code
                raise BadInput("Arguments were not given properly")
            else:
                # TODO make status code response instead
                raise NoInput("Name was Empty in Request")
    else:
        # TODO make status code response instead
        raise NoInput("Header was Empty in Request")
